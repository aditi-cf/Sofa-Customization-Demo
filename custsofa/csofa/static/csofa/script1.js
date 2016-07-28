(function (){

        var app = angular.module("csofa",[]);
        var MainController = function($scope,$http){
            $scope.sofa = furniture
            $scope.furniture = furniture
            $scope.priceCalculator = function(){
                $scope,furniture.price = 0;
                for (var key in furniture.components){
                    $scope.furniture.price += parseFloat(furniture.components[key]['properties']['price']);
                }
            }

            $scope.get_fun = function(sel_option,url_suffix,data){$http({
                        method: 'GET',
                        url: '/csofa/'+url_suffix,
                        params: data
                        })
                        .then(function successCallback(response) {
                            $scope.furniture.selectBar.value = response.data.data;
                            $scope.furniture.selectBar.name = sel_option;
                        },
                        function errorCallback(response) {
                            $scope.error = "Could Not fetch the" + sel_option;
                        }
                        );
            }

            $scope.getSelected = function(arg) {
                //change selectBar
                url_suffix = "";
                sel_option = "";

                for (url_suffix in arg){
                    sel_option = arg[url_suffix];
                }
                api_args = furniture.components[sel_option].apis[url_suffix];
                data = []
                for(var i in api_args){
                    data[i] = furniture.components[api_args[i]].properties[i]
                }

                $scope.get_fun(sel_option,url_suffix,data)

            }

            $scope.set_fun = function(sel_option,url_suffix,data){
                    $http({
                        method: 'GET',
                        url: '/csofa/'+url_suffix,
                        params: data
                        })
                        .then(function successCallback(response) {
                            resp = response.data.data;
                            $scope.furniture.components[sel_option].properties = resp[0]
                        },
                        function errorCallback(response) {
                            $scope.error = "Could Not Update the" + sel_option;
                        }
                        );
            }

            $scope.setSelected = function(arg,sel_item){

                sel_opt = $scope.furniture.selectBar.name;
                $scope.furniture.components[sel_opt].properties = sel_item;
                dependents = $scope.furniture.components[sel_opt].dependents
                for(var i=0; i < dependents.length; i += 1 ){
                    for(comp in dependents[i]){
                        for(api in dependents[i][comp]){
                            data = {}
                            for(api_args in dependents[i][comp][api]){
                                data[api_args] = $scope.furniture.components[dependents[i][comp][api][api_args]].properties[api_args]
                            }
                            $scope.set_fun(comp,api,data)
                        }
                    }
                }
                $scope.priceCalculator()
            }
        }

        app.controller("MainController",MainController);
    }
)();


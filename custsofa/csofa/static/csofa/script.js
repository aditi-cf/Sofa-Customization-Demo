(function (){

        var app = angular.module("csofa",[]);
        var MainController = function($scope,$http){
            $scope.tooloptions = ["Size","Arm","Arm Color","Back","Back Color","Pipe","Pipe Color","Leg","Leg Color"];
            $scope.selectBar = selectBar
            $scope.sofa = sofa

            $scope.priceCalculator = function(){
                console.log(parseFloat(sofa[0].arm.price,10)  + parseFloat(sofa[1].back.price,10) + parseFloat(sofa[2].leg.price,10) + parseFloat(sofa[3].pipe.price,10))
                $scope.price = parseFloat(sofa[0].arm.price,10)  + parseFloat(sofa[1].back.price,10) + parseFloat(sofa[2].leg.price,10) + parseFloat(sofa[3].pipe.price,10)
            }

            $scope.get_fun = function(sel_option,url_suffix,data){$http({
                        method: 'GET',
                        url: '/csofa/'+url_suffix,
                        params: data
                        })
                        .then(function successCallback(response) {
                            $scope.selectBar.options = response.data.data;
                            //console.log($scope.selectBar.options)
                            $scope.selectBar.selected_option = sel_option;
                        },
                        function errorCallback(response) {
                            $scope.error = "Could Not fetch the" + sel_option;
                        }
                        );
            }

            $scope.getSelected = function(arg) {
                //change selectBar
                if (arg == "Arm") {
                    data = {'size':$scope.sofa[0].arm.size,'color':$scope.sofa[0].arm.color,'back':$scope.sofa[1].back.back};
                    url_suffix = 'arm_all';
                    $scope.get_fun(arg,url_suffix,data);
                }
                else if (arg == "Arm Color") {
                    data = {'size':$scope.sofa[0].arm.size,'arm':$scope.sofa[0].arm.arm,'back':$scope.sofa[1].back.back}
                    url_suffix = 'arm_color_all';
                    $scope.get_fun(arg,url_suffix,data);
                }
                else if (arg == "Back") {
                    data = {'size':$scope.sofa[1].back.size,'arm':$scope.sofa[1].back.arm,'color':$scope.sofa[1].back.color}
                    url_suffix = 'back_all';
                    $scope.get_fun(arg,url_suffix,data);
                }
                else if (arg == "Back Color") {
                    data = {'size':$scope.sofa[1].back.size,'arm':$scope.sofa[1].back.arm,'back':$scope.sofa[1].back.back}
                    url_suffix = 'back_color_all';
                    $scope.get_fun(arg,url_suffix,data);
                }
                else if (arg == "Leg") {
                    data = {'size':$scope.sofa[2].leg.size,'arm':$scope.sofa[2].leg.arm}
                    url_suffix = 'leg_all';
                    $scope.get_fun(arg,url_suffix,data);
                }
                else if (arg == "Leg Color") {

                }
                else if (arg == "Pipe") {
                    data = {'size':$scope.sofa[3].pipe.size,'arm':$scope.sofa[3].pipe.arm,'back':$scope.sofa[3].pipe.back,'color':$scope.sofa[3].pipe.color}
                    url_suffix = 'pipe_all';
                    $scope.get_fun(arg,url_suffix,data);
                }
                else if (arg == "Pipe Color") {
                    data = {'size':$scope.sofa[3].pipe.size,'arm':$scope.sofa[3].pipe.arm,'back':$scope.sofa[3].pipe.back,'pipe':$scope.sofa[3].pipe.pipe}
                    url_suffix = 'pipe_color_all';
                    $scope.get_fun(arg,url_suffix,data);
                }
                else if (arg == "Size") {

                }
            }

            $scope.set_fun = function(sel_option,url_suffix,data){
                    $http({
                        method: 'GET',
                        url: '/csofa/'+url_suffix,
                        params: data
                        })
                        .then(function successCallback(response) {
                            resp = response.data.data;
                            if(sel_option == "Arm" && url_suffix == "back_all"){
                                sofa[1].back = resp[0];
                            }
                            else if(sel_option == "Arm" && url_suffix == "leg_all"){
                                sofa[2].leg = resp[0];
                            }
                            else if(sel_option == "Pipe" && url_suffix == "pipe_all"){
                                sofa[3].pipe = resp[0];
                            }
                        },
                        function errorCallback(response) {
                            $scope.error = "Could Not Update the" + sel_option;
                        }
                        );
            }

            $scope.setSelected = function(arg){
                if ($scope.selectBar.selected_option == "Arm") {
                    sofa[0].arm = arg;

                    data = {'size':sofa[0].arm.size,'color':'green','arm':sofa[0].arm.arm};
                    $scope.set_fun('Arm','back_all',data);

                    data = {'size':sofa[0].arm.size,'arm':sofa[0].arm.arm};
                    $scope.set_fun('Arm','leg_all',data);

                    data = {'size':sofa[0].arm.size,'arm':sofa[0].arm.arm,'color':'lightgreen','back':sofa[1].back.back};
                    $scope.set_fun('Pipe','pipe_all',data);
                }
                else if ($scope.selectBar.selected_option == "Arm Color") {
                    sofa[0].arm = arg;
                }
                else if ($scope.selectBar.selected_option == "Back") {
                    sofa[1].back = arg;
                    data = {'size':sofa[0].arm.size,'arm':sofa[0].arm.arm,'color':'lightgreen','back':sofa[1].back.back};
                    $scope.set_fun('Pipe','pipe_all',data);
                }
                else if ($scope.selectBar.selected_option == "Back Color") {
                    sofa[1].back = arg;
                }
                else if ($scope.selectBar.selected_option == "Leg") {
                    sofa[2].leg = arg;

                }
                else if ($scope.selectBar.selected_option == "Leg Color") {

                }
                else if ($scope.selectBar.selected_option == "Pipe") {
                    sofa[3].pipe = arg;
                }
                else if ($scope.selectBar.selected_option == "Pipe Color") {
                    sofa[3].pipe = arg;
                }
                else if (arg == "Size") {

                }

                $scope.priceCalculator()

            }


            /*

                {
                    furniture_name:sofa
                    comp-{
                        'name':'arm';
                        'properties': [{'':''},{'':''}]
                        'dependents': ['','','']
                        'apis': ['','','']
                        'api_args': [[],[],[]]
                    }
                }
            */
        /*
            $scope.callAPI(sel_option,url_suffix,data){
                var resp;
                $http({
                    method: 'GET',
                    url: '/csofa/'+url_suffix,
                    params: data
                }).then(function successCallback(response) {
                        resp = response.data.data[0];
                    },function errorCallback(response) {
                        $scope.error = "Could Not Update the" + sel_option;
                    }
                );


            }

            $scope.changeComponent = function(comp, flag, index){

                if(index == 0){ //shape change
                    if(flag == []){
                        sofa[comp.name] = comp;
                        flag.push(comp);
                    }
                    else{
                        url_suffix = comp.apis[0];
                        for(var j=0; j < comp.api_args.length; i += 1){
                            data[comp.api_args[j]] = sofa[comp.name][]
                        }
                    }
                    for(var i=0; i < comp.dependent.length; i += 1){

                        changeComponent(sofa[comp.dependent[i]],flag,index);
                    }
                }
                else{   //color change
                    sofa[comp.name] = comp;
                }


            };
        */

        }

        app.controller("MainController",MainController);
    }
)();


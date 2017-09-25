// app.js
// create our angular app and inject ngAnimate and ui-router 
// =============================================================================
angular.module('main', ['ui.router'])


// configuring our routes 
// =============================================================================
.config(function($stateProvider, $urlRouterProvider) {

	$stateProvider

        // route to show our basic form (/form)
	.state('form', {
		url: '/form',
		templateUrl: 'static/form.html',
		controller: 'formController'
	})

	// nested states 
	// each of these sections will have their own view
	// url will be /form/payment
	.state('form.login', {
		url: '/login',
		templateUrl: 'static/auth/login.html',
		controller: function($scope, $http) {
			$scope.showRegisterForm = true;
			$scope.user = {
				'email': 'example@test.com',
				'password': ''
			};
			$scope.errorMessage = "";
			$scope.auth = {};
			$scope.switchForm = function() {
				$scope.showRegisterForm = !$scope.showRegisterForm;
			};
			$scope.validPasswd = function() {
				return $scope.formData.passwd.length > 7 && $scope.pwMatch();
			}

			$scope.validEmail = function() {
				return /[A-z!-+]+@[A-z!-+]+\.\w+/.test($scope.formData.email);
			}

			$scope.pwMatch = function() {
				return $scope.formData.passwd === $scope.formData.passwd2;
			};
			$scope.auth.register = function(user) {
				try {
					$http.post('/users', {
						email: user.email,
						passwd: user.password
					}).then(function success(response) {
						console.log("Success");
					}, function failure(response) {
						console.log("Failure: " + response.data.message);
						$scope.errorMessage = response.data.message;
					});
				} catch(err) {
					console.log(err);
				}
			};
		}
	})

	// url will be nested (/form/profile)
	.state('form.profile', {
		url: '/profile',
		templateUrl: 'static/form-profile.html'
	})

	// url will be /form/interests
	.state('form.interests', {
		url: '/interests',
		templateUrl: 'static/form-interests.html'
	});


	$urlRouterProvider.otherwise('/form/login');
})

// our controller for the form
// =============================================================================
.controller('formController', function($scope) {

	// we will store all of our form data in this object
	$scope.formData = {
	'passwd': 'shit',
	};
	
	// function to process the form


});

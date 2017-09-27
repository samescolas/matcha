// app.js
// create our angular app and inject ngAnimate and ui-router 
// =============================================================================
angular.module('main', ['ui.router'])


// configuring our routes 
// =============================================================================
.config(function($stateProvider, $urlRouterProvider) {

	$stateProvider

	.state('login', {
		url: '/login',
		views: {
			'navbar' : {
				templateUrl: 'static/header.html',
				controller: 'navbarController'
			},
			'body' : {
				templateUrl: 'static/auth/login.html',
				controller: function($scope, $http) {
					$scope.showRegisterForm = true;
					$scope.user = {
						'email': 'example@test.com'
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
						$http.post('/users', {
							email: user.email,
							passwd: user.password
						}).then(function success(response) {
							$scope.$parent.formData.user = user.email;
							$scope.$parent.formData.passwd = user.password;
							console.log("Success");
						}, function failure(response) {
							console.log("Failure: " + response.data.message);
							$scope.errorMessage = response.data.message;
						});
					};
				}
			}
		}
	})

	.state('users', {
		url: '/users',
		views : {
			'navbar': {
				templateUrl: 'static/header.html',
				controller: 'navbarController'
			},
			'body': {
				templateUrl: 'static/users.html',
				controller: 'usersController'
			}
		}
	})

	.state('home', {
		abstract: true,
		url: '/home',
		views: {
			'navbar' : {
				templateUrl: 'static/header.html',
				controller: 'navbarController'
			},
			'body' : {
				templateUrl: 'static/form.html',
				controller: 'formController'
			}
		}
	})
	
	// nested states 
	// each of these sections will have their own view
	// url will be /form/payment
	.state('home.profile', {
		url: '/profile',
		templateUrl: 'static/form-profile.html',
		controller: 'formController'
	})

	// url will be /form/interests
	.state('home.interests', {
		url: '/interests',
		templateUrl: 'static/form-interests.html'
	})

	// url will be nested (/form/profile)
	.state('home.payment', {
		url: '/payment',
		templateUrl: 'static/form-payment.html'
	})

	.state('something', {
		url: '/something',
		views: {
			'navbar' : {
				templateUrl: "static/header.html"
			},
			'form' : {
				templateUrl: "static/header-search.html"
			}
		}
	});

	$urlRouterProvider.otherwise('/login');
})

// our controller for the form
// =============================================================================
.controller('navbarController', function($scope) {
	$scope.links = {};
})

.controller('formController', function($scope) {

	// we will store all of our form data in this object
	$scope.formData = {
	};
	
	// function to process the form


});

// app.js
// create our angular app
// =============================================================================
var app = angular.module('mainApplication', ["ngRoute", "ngCookies"]);

app.config(function($routeProvider) {
	$routeProvider
	.when("/", {
		templateUrl : "static/form-register.html"
	})
	.when("/register", {
		templateUrl: "static/form-interests.html"
	})
	.when("/login", {
		templateUrl: "static/form-login.html",
		controller: function($scope) {
				$scope.username = "user";
		}
	});
});

app.directive('matchaHeader', function() {

	var ctrl = ['$scope', function($scope) {
		$scope.links = [
			{'name' : 'home', 'nav' : '/'},
			{'name' : 'login', 'nav' : '/#!/login'},
			{'name' : 'register', 'nav' : '/#!/register'}
		];
	}];
	return {
		restrict: "E",
		templateUrl : "static/header.html",
		controller: ctrl
	};
});

// =============================================================================
app.controller('formController', ['$scope', function($scope) {

	// we will store all of our form data in this object
	$scope.formData = {};

	// function to process the form
	$scope.processForm = function(isValid) {
		if (isValid) {
			alert('awesome!');
		} else {
			alert('fix it!');
		}
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

}]);


app.run(function($rootScope, $cookies, $location) {
	$rootScope.$on('$routeChangeStart', function() {
		let cook = $cookies.get('loggedIn');
		if (cook) {
			$location.path('/#!/login');
		}
	});
});
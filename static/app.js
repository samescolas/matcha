// app.js
// create our angular app
// =============================================================================
var app = angular.module('formApp', ["ngRoute"]);

app.config(function($routeProvider) {
	$routeProvider
	.when("/", {
		templateUrl : "static/form-profile.html"
	})
	.when("/payment", {
		templateUrl: "static/form-payment.html"
	});
});

// =============================================================================
app.controller('formController', function($scope) {

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

});

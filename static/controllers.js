angular.module('main.controllers', [])

.controller('navbarController', function($scope) {
	$scope.links = {};
})

.controller('regController', function($scope, $http) {
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
})

.controller('formController', function($scope) {

	// we will store all of our form data in this object
	$scope.formData = {
	};
	
	// function to process the form
});

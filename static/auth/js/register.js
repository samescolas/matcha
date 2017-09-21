// register.js
// =============================================================================
angular.module('regApp', [])

// our controller for the form
// =============================================================================
.controller('regCtrl', function($scope, $http) {

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
	};

	$scope.validEmail = function() {
		return /[A-z!-+]+@[A-z!-+]+\.\w+/.test($scope.formData.email);
	};

	$scope.pwMatch = function() {
		return $scope.formData.passwd === $scope.formData.passwd2;
	};

	$scope.registerUser = function() {
		if ($scope.validEmail() && $scope.validPasswd()) {
			$http({
				method: 'POST',
				url: '/users',
				data: "{'email': " + $scope.formData.email + "}"
			}).then(function(response) {
				alert("registered!");
				$scope.formData['response'] = response;
			}, function(response) {
				alert("no bueno.");
			});
		} else {
			alert("invalid form!");
		}
	};

});

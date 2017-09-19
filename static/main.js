(function () {
	'use strict';

	angular.module('main', [])
	.controller('main-controller', ['$scope', function($scope) {
		$scope.message = "hey there";
	}]);
}());

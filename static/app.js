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
	// url will be nested (/form/profile)
	.state('form.profile', {
		url: '/profile',
		templateUrl: 'static/form-profile.html'
	})

	// url will be /form/interests
	.state('form.interests', {
		url: '/interests',
		templateUrl: 'static/form-interests.html'
	})

	// url will be /form/payment
	.state('form.payment', {
		url: '/payment',
		templateUrl: 'static/form-payment.html'
	});

	$urlRouterProvider.otherwise('/form/profile');
})

// our controller for the form
// =============================================================================
.controller('formController', function($scope) {

	// we will store all of our form data in this object
	$scope.formData = {
	'passwd': ''
	};

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

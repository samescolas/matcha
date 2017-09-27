// app.js
// create our angular app and inject ngAnimate and ui-router 
// =============================================================================
angular.module('main', ['ui.router', 'main.controllers'])


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
				controller: 'regController'
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
});

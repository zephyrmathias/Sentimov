angular.module('sentiMov', ['sentiMov.controller', 'sentiMov.services', 'sentiMov.directives'])

.config(function($interpolateProvider, $locationProvider, $sceDelegateProvider) {
    $locationProvider.html5Mode({
      enabled: true,
      requireBase: false
    });
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    $sceDelegateProvider.resourceUrlWhitelist([
      'self',
      'https://www.youtube.com/**'
    ]);
});

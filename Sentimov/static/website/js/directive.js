angular.module('sentiMov.directives', [])

.directive("repeatEnd", function(){
  return {
    restrict: "A",
    link: function (scope, element, attrs) {
      if (scope.$last) {
        scope.$eval(attrs.repeatEnd);
      }
    }
  };
})

.directive('errorImg', function () {
  return {
    restrict: 'A',
    link: function (scope, element, attrs) {
      element.bind('error', function() {
        var url = "https://s7.postimg.org/jnyp8zv8r/default_poster.jpg";
        element.prop('src', url);
      });
    }
  }
})

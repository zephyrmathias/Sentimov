angular.module('sentiMov.controller', ['sentiMov.services', 'sentiMov.directives'])

.controller('HomeCtrl', function($scope, $window){
  $scope.movie_name = "";
  $scope.search = function(movie_name){
    if (movie_name == "") {
      return;
    }
    $window.location.href = "/search?moviename=" + movie_name
  }
})

.controller('SearchCtrl', function($scope, $location, MovieApi, $window, $timeout){
  var movie_name = $location.search().moviename;
  MovieApi.searchMovie(movie_name).then(function(response){
    console.log(response);
    $scope.search_results = response.data;
  })

  $scope.onEnd = function(){
    $timeout(function(){
      var swiper = new Swiper('.swiper-container', {
          pagination: '.swiper-pagination',
          centeredSlides: true,
          paginationClickable: true,
          spaceBetween: 0,
          slidesPerView: 1,
      });
      }, 1);
    };

  $scope.get_twt = function(title,id){
    $window.location.href = "/tweet?moviename=" + title + "&id=" + id;
  }
})

.controller('TweetCtrl', function($scope, $location, $http){
  $scope.movie_name = $location.search().moviename;
  $scope.movie_id = $location.search().id;
  var maxid = -1;
  $scope.tweet = [];
  $scope.count = 0;
  $scope.which_btn = 0;
  $scope.stop_getting = 0;
  $scope.no_tweets = 0;
  $scope.stop_btn = function(){
    $scope.stop_getting = 1;
  }

  function makeNextRequest(){
    $http({method: 'GET', url: '/apitweet?moviename=' + $scope.movie_name + '&maxid=' + maxid})
    .then(function(response){
      console.log(maxid);
      if (response.data.hasOwnProperty('test') && $scope.stop_getting == 0) {
        maxid = response.data.maxid;
        $scope.count = $scope.count + response.data.count;
        angular.forEach(response.data.test, function(value){
          $scope.tweet.push(value);
        })
        makeNextRequest();
      }
      else {
        $scope.count = $scope.count + response.data.count;
        angular.forEach(response.data.test, function(value){
          $scope.tweet.push(value);
        })
        $scope.which_btn = 1;
        $scope.no_tweets = 1;
      }
    },
    function(err){
      $scope.which_btn = 1;
    })
  }

    $http({method: 'GET', url: '/delete?moviename=' + $scope.movie_name}).then(function(response){
      if(response.data.done == "done") {
        makeNextRequest();
      }
    })

})

.controller('ResultCtrl', function($scope, $location, $http, MovieApi, Sentiment, $timeout, $window){
  var movie_name = $location.search().moviename;
  var movie_id = $location.search().id;
  $scope.neu_width = 0;
  $scope.pos_width = 0;
  $scope.neg_width = 0;
  $scope.sentiment_done = false;
  MovieApi.getMovieDetail(movie_id).then(function(response){
    $scope.movie_detail = response.data;
    $scope.runtime_hours = Math.floor(response.data.runtime / 60);
    $scope.runtime_mins = response.data.runtime - ($scope.runtime_hours * 60);
  });
  MovieApi.getMovieCast(movie_id).then(function(response){
    $scope.movie_cast = response.data;
  });
  MovieApi.getVideo(movie_id).then(function(response){
    $scope.video = response.data;
  });
  MovieApi.getMovieRecommend(movie_id).then(function(response){
    $scope.recommend = response.data;
  });
  var myDataPromise = Sentiment.getSentimentResult(movie_name);
  myDataPromise.then(function(response){
    $scope.sentiment_result = response.data;
    $scope.pos_tweets = $scope.sentiment_result['pos'];
    $scope.neg_tweets = $scope.sentiment_result['neg'];
    $scope.neu_tweets = $scope.sentiment_result['neu'];
    $scope.total_tweets = $scope.pos_tweets.length + $scope.neg_tweets.length + $scope.neu_tweets.length
    $scope.neu_width = (($scope.neu_tweets.length * 100)/$scope.total_tweets).toString() + "%";
    $scope.pos_width = (($scope.pos_tweets.length * 100)/$scope.total_tweets).toString() + "%";
    $scope.neg_width = (($scope.neg_tweets.length * 100)/$scope.total_tweets).toString() + "%";
    $scope.sentiment_done = true;
  })


  $scope.menu_toggle = 1;
  $scope.toggle = function(val) {
    $scope.menu_toggle = val;
  }

  $scope.getIframeSrc = function(key){
    return 'https://www.youtube.com/embed/' + key;
  }
  
  $scope.download = function(){
    $window.location.href = "/download?moviename=" + movie_name;
  }

})

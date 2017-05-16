angular.module('sentiMov.services', [])

.factory('MovieApi', function($http){
  api_key = '7d9a917a17fe50bddf011ece92641a3a';
  return {
    getApiKey: function(){
      return api_key;
    },
    searchMovie: function(movie_name){
      return $http.get('https://api.themoviedb.org/3/search/multi?api_key=' + api_key +'&query=' + movie_name).then(function(response){
        return response;
      })
    },
    getMovieDetail: function(movie_id){
      return $http.get('https://api.themoviedb.org/3/movie/' + movie_id + '?api_key=' + api_key).then(function(response){
        return response;
      })
    },
    getMovieCast: function(movie_id){
      return $http.get('https://api.themoviedb.org/3/movie/' + movie_id + '/credits?api_key=' + api_key).then(function(response){
        return response;
      })
    },
    getVideo: function(movie_id){
      return $http.get('https://api.themoviedb.org/3/movie/' + movie_id + '/videos?api_key=' + api_key).then(function(response){
        return response;
      })
    },
    getMovieRecommend: function(movie_id){
      return $http.get('https://api.themoviedb.org/3/movie/' + movie_id + '/recommendations?api_key=' + api_key).then(function(response){
        return response;
      })
    }
  }
})

.factory('Sentiment', function($http){
  return {
    getSentimentResult: function(movie_name){
      return $http.get('/sentiment?moviename=' + movie_name).then(function(response){
        return response;
      })
    }
  }
})

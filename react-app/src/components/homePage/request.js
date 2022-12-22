const API_KEY = "64d0d89ae0c4a38fef2b26b6e630a66c";

const requests = {
    fetchNetflixOriginals: `/discover/tv?api_key=${API_KEY}&with_networks=213`,
    fetchTrendingNow: `/movie/popular?api_key=${API_KEY}&language=en-US&page=1`,
    fetchTop: `/movie/top_rated?api_key=${API_KEY}&language=en-US&page=1`,
    fetchDramas: `/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10`,
    fetchComedyMovies: `/discover/movie?api_key=${API_KEY}&with_genres=35`,
    fetchActionMovies: `/discover/movie?api_key=${API_KEY}&with_genres=28`,
    fetchHorrorMovies: `/discover/movie?api_key=${API_KEY}&with_genres=27`,
    fetchRomanceMovies: `/discover/movie?api_key=${API_KEY}&with_genres=10749`,
    fetchDocumentaries: `/discover/movie?api_key=${API_KEY}&with_genres=99`
    // fetchMovieDetails: `https://api.themoviedb.org/3/movie/343611?api_key=${API_KEY}`
    // fetchKids: `/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc`
}

export default requests;

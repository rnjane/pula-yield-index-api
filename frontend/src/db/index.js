const config = {
	headers: {
	  Authorization: `Token ${window.localStorage.getItem('token')}`,
	  'content-Type': 'application/json',
	},
	BASE_URL: 'http://127.0.0.1:8000',
  };
  
  export default config;
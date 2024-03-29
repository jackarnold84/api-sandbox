// fetch data from external APIs

const wikiSearch = async (search) => {

  apiUrl = 'https://p8q5t9dto5.execute-api.us-east-2.amazonaws.com/default/wikiSearch';

  return fetch(apiUrl + '?' + new URLSearchParams(
    {
      'search': search,
    }
  ),
    {
      'method': 'GET',
    }
  )
    .then(response => response.json())
    .catch(error => console.warn(error))
};


const publicForumAPI = async (action, post = '') => {

  apiUrl = 'https://p8q5t9dto5.execute-api.us-east-2.amazonaws.com/default/publicForum';

  return fetch(apiUrl + '?' + new URLSearchParams(
    {
      'action': action,
      'post': post,
    }
  ),
    {
      'method': 'GET',
    }
  )
    .then(response => response.json())
    .catch(error => console.warn(error))
};


const dataSummarizerAPI = async (fileContent) => {

  apiUrl = 'https://p8q5t9dto5.execute-api.us-east-2.amazonaws.com/default/dataSummarizer';

  return fetch(apiUrl + '?' + new URLSearchParams(
    {
      'fileContent': fileContent,
    }
  ),
    {
      'method': 'GET',
    }
  )
    .then(response => response.json())
    .catch(error => console.warn(error))
};


const secretMessageAPI = async (token) => {
  apiUrl = 'https://p8q5t9dto5.execute-api.us-east-2.amazonaws.com/default/secretMessage';

  return fetch(apiUrl + '?' + new URLSearchParams(
    {
      'action': 'getSecretMessage',
    }
  ),
    {
      'method': 'POST',
      'body': JSON.stringify({'auth': {'token': token}}),
    }
  )
    .then(response => response.json())
    .catch(error => console.warn(error))
};

const secretMessageCheckAuthAPI = async (token) => {
  // returns returns {'authorized': bool}
  apiUrl = 'https://p8q5t9dto5.execute-api.us-east-2.amazonaws.com/default/secretMessage';

  return fetch(apiUrl + '?' + new URLSearchParams(
    {
      'auth': 'checkAuth',
    }
  ),
    {
      'method': 'POST',
      'body': JSON.stringify({'auth': {'token': token}}),
    }
  )
    .then(response => response.json())
    .catch(error => console.warn(error))
};

const secretMessageRequestAuthTokenAPI = async (password) => {
  // returns {'authorized': bool, 'token': string}
  apiUrl = 'https://p8q5t9dto5.execute-api.us-east-2.amazonaws.com/default/secretMessage';

  return fetch(apiUrl + '?' + new URLSearchParams(
    {
      'auth': 'requestAuth',
    }
  ),
    {
      'method': 'POST',
      'body': JSON.stringify({'auth': {'password': password}}),
    }
  )
    .then(response => response.json())
    .catch(error => console.warn(error))
};

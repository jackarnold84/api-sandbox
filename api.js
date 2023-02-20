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

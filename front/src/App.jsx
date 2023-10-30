import React, { useState } from 'react'
import api from './api'
import Spinning from './Spinning';

function App() {
  const [formData, setFormData] = useState({
    series_or_movie: 'TV series',
    genre: 'Action',
    decade: '2020',
    age_rating: 'General Audiences',
    positive_reference: '',
    negative_reference: '',
  });
  const [recommendation, setRecommendation] = useState('');
  const [isLoading, setIsLoading] = useState(false);


  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    setIsLoading(true)

    api.getRecommendation(formData).then((value) => {
      setRecommendation(value)
      setIsLoading(false);
      console.log(value)
    })
  };

  return (
    <main className='flex flex-col items-center justify-center gap-4 font-poppins 
     bg-red-700 w-full h-screen'>
      <h1 className='text-white flex items-center text-5xl font-bold uppercase'>Flix Finder
        <span className='ml-2 text-3xl'>📽️</span>
        <span className='text-4xl'>🍿</span>
      </h1>

      <div className='w-3/5 h-4/5 bg-white px-10 py-8 rounded-3xl shadow-md shadow-slate-900/70 overflow-hidden'>
        <form onSubmit={handleSubmit} className='flex flex-col gap-3 text-xl'>
          <label>
            Series or Movie:
            <select name="series_or_movie" value={formData.series_or_movie} onChange={handleInputChange}
              className='border border-black rounded-md p-2 ml-4'>
              <option value="TV series">TV series</option>
              <option value="Movie">Movie</option>
            </select>
          </label>

          <label>
            Genre:
            <select name="genre" value={formData.genre} onChange={handleInputChange}
              className='border border-black rounded-md p-2 ml-4'>
              <option value="Action">Action</option>
              <option value="Adventure">Adventure</option>
              <option value="Comedy">Comedy</option>
              <option value="Drama">Drama</option>
              <option value="Fantasy">Fantasy</option>
              <option value="Science Fiction">Science Fiction</option>
              <option value="Horror">Horror</option>
              <option value="Romance">Romance</option>
              <option value="Animation">Animation</option>
              <option value="Crime">Crime</option>
              <option value="Documentary">Documentary</option>
              <option value="Suspense">Suspense</option>
              <option value="Musical">Musical</option>
              <option value="Mystery">Mystery</option>
              <option value="War">War</option>
              <option value="Western">Western</option>
              <option value="Thriller">Thriller</option>
              <option value="History">History</option>
              <option value="Sport">Sport</option>
              <option value="Talk Show">Talk Show</option>
              <option value="Reality Show">Reality Show</option>
              <option value="Superhero">Superhero</option>
            </select>
          </label>

          <label>
            Decade:
            <select name="decade" value={formData.decade} onChange={handleInputChange}
              className='border border-black rounded-md p-2 ml-4'>
              <option value="2020">2020</option>
              <option value="2010">2010</option>
              <option value="2000">2000</option>
              <option value="1990">1990</option>
              <option value="1980">1980</option>
              <option value="1970">1970</option>
              <option value="1960">1960</option>
              <option value="1950">1950</option>
              <option value="1940">1940</option>
              <option value="1930">1930</option>
              <option value="1920">1920</option>
              <option value="1910">1910</option>
            </select>
          </label>

          <label>
            Age Rating:
            <select name="age_rating" value={formData.age_rating} onChange={handleInputChange}
              className='border border-black rounded-md p-2 ml-4'>
              <option value="General Audiences">General Audiences</option>
              <option value="Parental Guidance Suggested">Parental Guidance Suggested</option>
              <option value="Parents Strongly Cautioned">Parents Strongly Cautioned</option>
              <option value="Restricted">Restricted</option>
              <option value="Adults Only">Adults Only</option>
            </select>
          </label>

          <label>
            Positive Reference:
            <input
              type="text"
              name="positive_reference"
              value={formData.positive_reference}
              onChange={handleInputChange}
              className='border border-black rounded-md p-2 ml-4'
            />
          </label>

          <label>
            Negative Reference:
            <input
              type="text"
              name="negative_reference"
              value={formData.negative_reference}
              onChange={handleInputChange}
              className='border border-black rounded-md p-2 ml-4'
            />
          </label>

          <button type="submit" disabled={isLoading}
            className='relative bg-red-600 hover:bg-red-600/90 disabled:bg-red-500 disabled:cursor-not-allowed
           w-56 h-16 gap-2 rounded-xl mt-3 text-white shadow-sm shadow-slate-900/50 flex justify-center items-center'>
            Send
            {isLoading && <Spinning />}
          </button>
        </form>

        {recommendation && !isLoading &&
          <div className='mt-6 max-h-[30%] overflow-auto border-2 border-slate-900 px-3 py-2 rounded-md'>
            <p className='text-xl'>
              {recommendation}
            </p>
          </div>}
      </div>
    </main>
  );
}

export default App

import Head from 'next/head'
import { useState } from 'react';
import 'tailwindcss/tailwind.css'
import * as api from '../api';

export default function Home() {
  
  const [currentlyDisplayedCommentContent, setCurrentlyDisplayedCommentContent] = useState('Random github comments every day');
  const [currentlyDisplayedCommentSource, setCurrentlyDisplayedCommentSource] = useState('');
  
  
  const getComment = async () => {
    const comment = await api.getComment();
    setCurrentlyDisplayedCommentContent(comment.content);
    setCurrentlyDisplayedCommentSource(comment.url);
  }
  
  const displayLinkIfNeeded = () => {
    if(!['', 'Unavailable'].includes(currentlyDisplayedCommentSource)) {
      return (
        <p className='hover:underline'><a href={currentlyDisplayedCommentSource}>Source</a></p>
      )
    }
    return '';
  }
  
  return (
    <div className='flex flex-wrap w-screen h-screen bg-gray-900 text-white' >
      <Head>
        <title>Random github</title>
        <link rel='icon' href='/favicon.ico' />
      </Head>

      <main className='m-auto w-full md:w-1/2'>
        <div className='text-center'>
          <p className='text-2xl md:text-3xl p-2 my-2'>{currentlyDisplayedCommentContent}</p>
          <button 
            className=' p-2 bg-blue-500 hover:bg-blue-700 text-white text-xl md:text-2xl font-bold py-2 px-4 rounded-full'
            onClick={getComment}
          >
            Get random comment
          </button>
        </div>
        <p>{displayLinkIfNeeded()}</p>
        <div>
          
        </div>
      </main>

      <footer>
      </footer>
    </div>
  )
}

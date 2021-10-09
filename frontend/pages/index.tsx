import Head from 'next/head'
import { useState } from 'react';
import 'tailwindcss/tailwind.css'
import * as api from '../api';
import ClipLoader from "react-spinners/ClipLoader";

export default function Home() {  
  const [currentlyDisplayedCommentContent, setCurrentlyDisplayedCommentContent] = useState('Random github comments every day');
  const [currentlyDisplayedCommentSource, setCurrentlyDisplayedCommentSource] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  
  const getComment = async () => {
    setIsLoading(true);
    const comment = await api.getComment();
    setCurrentlyDisplayedCommentContent(comment.content);
    setCurrentlyDisplayedCommentSource(comment.url);
    setIsLoading(false);
  }
  
  const displayLinkIfNeeded = () => {
    if(!['', 'Unavailable'].includes(currentlyDisplayedCommentSource)) {
      return (
        <div>
          <p className='hover:underline hidden sm:block'><a href={currentlyDisplayedCommentSource}><b>Source</b>: {currentlyDisplayedCommentSource}</a></p>
          <p className='hover:underline sm:hidden text-xl'><a href={currentlyDisplayedCommentSource}><b><u>Source</u></b></a></p>
        </div>
      )
    }
    return '';
  }
  
  return (
    <div className='flex flex-wrap w-screen h-screen bg-gray-900 text-white font-mono' >
      <Head>
        <title>Random github</title>
        <link rel='icon' href='/favicon.ico' />
      </Head>

      <main className='m-auto w-2/3 sm:w-full'>
        <div className='text-left sm:text-center p-2 my-2'>
          <p className='text-2xl md:text-3xl'>{currentlyDisplayedCommentContent}</p>
          <div className='mt-5 text-center'>
            <ClipLoader loading={isLoading} color='white' size={45}/>
          </div>
          <div className='mt-5'>
            <button 
              className=' bg-blue-500 hover:bg-blue-700 text-white text-xl md:text-2xl font-bold py-4 px-6 rounded-full mb-5'
              onClick={getComment}
            >
              Get random comment
            </button>
            <p>{displayLinkIfNeeded()}</p>
          </div>
        </div>
        <div>
          
        </div>
      </main>

      <footer>
      </footer>
    </div>
  )
}

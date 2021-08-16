import Head from 'next/head'
import 'tailwindcss/tailwind.css'

export default function Home() {
  const getComment = () => {
    console.log('getComment');
  }
  
  return (
    <div className='flex flex-wrap w-screen h-screen bg-gray-900 text-white' >
      <Head>
        <title>Random github</title>
        <link rel='icon' href='/favicon.ico' />
      </Head>

      <main className='m-auto'>
        <div className='text-center'>
          <p className='text-3xl p-2 my-2'>Random github comments every day</p>
          <button 
            className='w-full p-2 bg-blue-500 hover:bg-blue-700 text-white text-2xl font-bold py-2 px-4 rounded-full'
            onClick={getComment}
          >
            Get random comment
          </button>
        </div>
      </main>

      <footer>
      </footer>
    </div>
  )
}

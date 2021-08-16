import Head from 'next/head'
import 'tailwindcss/tailwind.css'

export default function Home() {
  return (
    <div className='flex flex-wrap w-screen h-screen' >
      <Head>
        <title>Random github</title>
        <link rel='icon' href='/favicon.ico' />
      </Head>

      <main className='m-auto'>
        <div className='text-center'>
          <p className='text-3xl'>Random github comments every day</p>
          <button className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full'>
            Get random comment
          </button>
        </div>
      </main>

      <footer>
      </footer>
    </div>
  )
}

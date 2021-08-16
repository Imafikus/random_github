import Head from 'next/head'
import 'tailwindcss/tailwind.css'

export default function Home() {
  return (
    <div className="flex flex-wrap w-screen" >
      <Head>
        <title>Random github</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className='m-auto'>
        <div>
          <p className='text-3xl'>Random github comments every day</p>
        </div>
      </main>

      <footer>
      </footer>
    </div>
  )
}

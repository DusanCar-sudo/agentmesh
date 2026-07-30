import dynamic from 'next/dynamic'
import Navbar from '@/components/Navbar'
import Hero from '@/components/Hero'
import Features from '@/components/Features'
import CTA from '@/components/CTA'
import Footer from '@/components/Footer'

// Dynamic import for 3D background to avoid SSR issues
const MeshBackground = dynamic(() => import('@/components/MeshBackground'), {
  ssr: false,
  loading: () => null,
})

export default function Home() {
  return (
    <main className="relative min-h-screen">
      <MeshBackground />
      <Navbar />
      <Hero />
      <Features />
      <CTA />
      <Footer />
    </main>
  )
}

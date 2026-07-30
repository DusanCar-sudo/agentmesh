import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  metadataBase: new URL('https://agentmesh-zeta.vercel.app'),
  title: 'Agent Mesh — Autonomous Programming Harness',
  description: 'A standalone, lightweight harness for autonomous programming, coding, refactoring, and debugging. Deploy AI agents that write, review, and fix code at scale.',
  keywords: ['AI', 'autonomous programming', 'code generation', 'refactoring', 'debugging', 'agent mesh', 'LLM', 'developer tools'],
  authors: [{ name: 'Agent Mesh' }],
  openGraph: {
    title: 'Agent Mesh — Autonomous Programming Harness',
    description: 'A standalone, lightweight harness for autonomous programming, coding, refactoring, and debugging.',
    type: 'website',
    locale: 'en_US',
    images: ['/og-image.png'],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Agent Mesh — Autonomous Programming Harness',
    description: 'A standalone, lightweight harness for autonomous programming, coding, refactoring, and debugging.',
    images: ['/og-image.png'],
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="dark">
      <body className={`${inter.className} bg-mesh-dark text-gray-100 antialiased`}>
        {children}
      </body>
    </html>
  )
}

'use client'

import { ArrowRight, Github, Terminal, BookOpen } from 'lucide-react'

export default function CTA() {
  return (
    <section id="get-started" className="relative py-32 overflow-hidden">
      {/* Background effects */}
      <div className="absolute inset-0 mesh-gradient opacity-50" />
      <div className="absolute inset-0 grid-pattern opacity-20" />

      <div className="relative max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        {/* Badge */}
        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-mesh-cyan/10 border border-mesh-cyan/20 mb-8">
          <Terminal className="w-4 h-4 text-mesh-cyan" />
          <span className="text-sm font-mono text-mesh-cyan">Open Source & Free Forever</span>
        </div>

        {/* Headline */}
        <h2 className="text-4xl sm:text-6xl font-bold text-white mb-6 drop-shadow-lg">
          Ready to deploy your
          <br />
          <span className="bg-gradient-to-r from-mesh-cyan to-mesh-purple bg-clip-text text-transparent">
            first agent mesh?
          </span>
        </h2>

        {/* Subheadline */}
        <p className="text-xl text-gray-200 max-w-2xl mx-auto mb-10">
          Get started in under 60 seconds. Zero configuration required.
          Just install, define your agents, and let them code.
        </p>

        {/* Install command */}
        <div className="code-block max-w-xl mx-auto mb-10 p-4 text-left">
          <div className="flex items-center justify-between mb-2">
            <span className="text-xs text-gray-500 font-mono">quick start</span>
            <button
              onClick={() => navigator.clipboard.writeText('npm install -g agentmesh && agentmesh init')}
              className="text-xs text-mesh-cyan hover:text-white transition-colors font-mono"
            >
              copy
            </button>
          </div>
          <code className="text-base">
            <span className="text-gray-500">$</span>{' '}
            <span className="text-mesh-cyan">npm</span>{' '}
            <span className="text-white">install -g agentmesh</span>
            <span className="text-gray-500"> && agentmesh init</span>
          </code>
        </div>

        {/* CTAs */}
        <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-16">
          <a
            href="https://github.com/DusanCar-sudo/agentmesh"
            target="_blank"
            rel="noopener noreferrer"
            className="btn-primary group flex items-center gap-2 px-8 py-4 bg-mesh-cyan text-mesh-dark font-semibold rounded-lg hover:bg-mesh-cyan/90 transition-all"
          >
            <Github className="w-5 h-5" />
            Star on GitHub
            <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
          </a>
          <a
            href="#"
            className="flex items-center gap-2 px-8 py-4 bg-white/5 border border-white/10 text-white font-semibold rounded-lg hover:bg-white/10 transition-all"
          >
            <BookOpen className="w-5 h-5" />
            Read the Docs
          </a>
        </div>

        {/* Trust badges */}
        <div className="flex flex-wrap items-center justify-center gap-8 text-gray-500 text-sm">
          <div className="flex items-center gap-2">
            <Shield className="w-4 h-4 text-mesh-green" />
            <span>MIT Licensed</span>
          </div>
          <div className="flex items-center gap-2">
            <Zap className="w-4 h-4 text-yellow-400" />
            <span>Type-Safe Contracts</span>
          </div>
          <div className="flex items-center gap-2">
            <GitBranch className="w-4 h-4 text-mesh-purple" />
            <span>Git-Native</span>
          </div>
        </div>
      </div>
    </section>
  )
}

function Shield(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
      <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
    </svg>
  )
}

function Zap(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
      <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" />
    </svg>
  )
}

function GitBranch(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
      <line x1="6" y1="3" x2="6" y2="15" />
      <circle cx="18" cy="6" r="3" />
      <circle cx="6" cy="18" r="3" />
      <path d="M18 9a9 9 0 0 1-9 9" />
    </svg>
  )
}

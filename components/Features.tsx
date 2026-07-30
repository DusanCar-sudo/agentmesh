'use client'

import { Code2, Bug, RefreshCw, Shield, Zap, GitBranch } from 'lucide-react'

const features = [
  {
    icon: Code2,
    title: 'Autonomous Coding',
    description: 'Agents that write production-ready code from natural language specs. Supports 20+ languages with context-aware generation.',
    color: 'text-mesh-cyan',
  },
  {
    icon: Bug,
    title: 'Intelligent Debugging',
    description: 'Automated root-cause analysis with stack trace parsing, log correlation, and fix suggestion. Reduces debug time by 80%.',
    color: 'text-mesh-purple',
  },
  {
    icon: RefreshCw,
    title: 'Smart Refactoring',
    description: 'Safe, incremental refactoring with AST-aware transformations. Preserves behavior while improving structure and performance.',
    color: 'text-mesh-blue',
  },
  {
    icon: Shield,
    title: 'Sandboxed Execution',
    description: 'Every agent runs in isolated containers with resource limits. Full audit trail with rollback on failure.',
    color: 'text-mesh-green',
  },
  {
    icon: Zap,
    title: 'Lightweight Core',
    description: 'Under 50MB runtime. No heavy orchestrator. Pure function agents that compose via typed contracts.',
    color: 'text-yellow-400',
  },
  {
    icon: GitBranch,
    title: 'Git-Native Workflow',
    description: 'Agents create branches, open PRs, and respond to review comments. Integrates with GitHub, GitLab, and Bitbucket.',
    color: 'text-orange-400',
  },
]

export default function Features() {
  return (
    <section id="features" className="relative py-32 overflow-hidden">
      {/* Background grid */}
      <div className="absolute inset-0 grid-pattern opacity-30" />

      <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section header */}
        <div className="text-center mb-20">
          <h2 className="text-4xl sm:text-5xl font-bold text-white mb-4">
            Built for <span className="text-mesh-cyan">autonomous</span> development
          </h2>
          <p className="text-xl text-gray-400 max-w-2xl mx-auto">
            Every component designed for reliability, speed, and developer experience.
          </p>
        </div>

        {/* Features grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {features.map((feature, index) => (
            <div
              key={index}
              className="feature-card group relative p-6 rounded-2xl bg-white/[0.02] backdrop-blur-sm"
            >
              {/* Icon */}
              <div className={`inline-flex items-center justify-center w-12 h-12 rounded-xl bg-white/5 mb-4 ${feature.color}`}>
                <feature.icon className="w-6 h-6" />
              </div>

              {/* Content */}
              <h3 className="text-xl font-semibold text-white mb-2 group-hover:text-mesh-cyan transition-colors">
                {feature.title}
              </h3>
              <p className="text-gray-400 leading-relaxed">
                {feature.description}
              </p>

              {/* Hover glow */}
              <div className="absolute inset-0 rounded-2xl bg-gradient-to-br from-mesh-cyan/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none" />
            </div>
          ))}
        </div>

        {/* Architecture diagram placeholder */}
        <div id="architecture" className="mt-32">
          <div className="text-center mb-12">
            <h3 className="text-3xl font-bold text-white mb-4">How It Works</h3>
            <p className="text-gray-400 max-w-xl mx-auto">
              Three specialized agents collaborate through typed contracts to deliver complete code solutions.
            </p>
          </div>

          <div className="code-block max-w-4xl mx-auto p-6 sm:p-8">
            <div className="flex items-center gap-2 mb-6">
              <div className="w-3 h-3 rounded-full bg-red-500/80" />
              <div className="w-3 h-3 rounded-full bg-yellow-500/80" />
              <div className="w-3 h-3 rounded-full bg-green-500/80" />
              <span className="ml-2 text-xs text-gray-500 font-mono">agent-mesh-architecture.ts</span>
            </div>
            <pre className="text-sm sm:text-base overflow-x-auto">
              <code>
                <span className="text-gray-500">// Agent Mesh Runtime</span>
                {'\n'}
                <span className="text-mesh-purple">const</span>{' '}
                <span className="text-white">mesh</span> ={' '}
                <span className="text-mesh-cyan">createMesh</span>({'{'}
                {'\n'}
                {'  '}<span className="text-white">agents</span>: [
                {'\n'}
                {'    '}{'{ '}<span className="text-mesh-green">name</span>: <span className="text-yellow-400">'architect'</span>,{' '}
                <span className="text-mesh-green">role</span>: <span className="text-yellow-400">'design'</span> {'}'},
                {'\n'}
                {'    '}{'{ '}<span className="text-mesh-green">name</span>: <span className="text-yellow-400">'coder'</span>,{' '}
                <span className="text-mesh-green">role</span>: <span className="text-yellow-400">'implement'</span> {'}'},
                {'\n'}
                {'    '}{'{ '}<span className="text-mesh-green">name</span>: <span className="text-yellow-400">'reviewer'</span>,{' '}
                <span className="text-mesh-green">role</span>: <span className="text-yellow-400">'validate'</span> {'}'},
                {'\n'}
                {'  '}],
                {'\n'}
                {'  '}<span className="text-mesh-green">contracts</span>: <span className="text-yellow-400">'strict'</span>,{' '}
                <span className="text-mesh-green">sandbox</span>: <span className="text-mesh-cyan">true</span>
                {'\n'}
                {'}'})
                {'\n'}
                {'\n'}
                <span className="text-gray-500">// Execute autonomous workflow</span>
                {'\n'}
                <span className="text-mesh-purple">const</span>{' '}
                <span className="text-white">result</span> ={' '}
                <span className="text-mesh-cyan">await</span>{' '}
                <span className="text-white">mesh</span>.
                <span className="text-mesh-cyan">run</span>(<span className="text-yellow-400">'Build REST API with auth'</span>)
              </code>
            </pre>
          </div>
        </div>
      </div>
    </section>
  )
}

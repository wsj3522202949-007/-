---
id: tool-00355
type: tool
area: 库
status: active
tags: [TypeScript, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: AI-Interactive-Story-Game-Generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/achrefrhm/ai-interactive-story-game-generator
created: 2026-07-18
updated: 2026-07-18
no: 355
category: 二、网文 / 长篇 AI 写作系统 库
repo: AchrefRhm/AI-Interactive-Story-Game-Generator
stars: 1
url: https://github.com/achrefrhm/ai-interactive-story-game-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AchrefRhm/AI-Interactive-Story-Game-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/achrefrhm/ai-interactive-story-game-generator
- **Stars**：1
- **语言**：TypeScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：AchrefRhm/AI-Interactive-Story-Game-Generator
- **拉取时间**：2026-07-23 22:49:28

---

# StoryForge - AI Interactive Story Game Generator

![StoryForge Banner](https://images.pexels.com/photos/256417/pexels-photo-256417.jpeg?auto=compress&cs=tinysrgb&w=1200)

## Overview

**StoryForge** is an immersive, AI-powered interactive story game where your choices shape the narrative. Create your character, embark on epic adventures, build meaningful relationships with NPCs, and watch as your decisions ripple through dynamically generated storylines.

### Created by Achref Rhouma

---

## Features

### Core Gameplay
- **Multiple Genres**: Choose from 6 exciting genres
  - Fantasy: Magical realms, ancient prophecies, epic quests
  - Sci-Fi: Space exploration, alien encounters, future technology
  - Mystery: Crime solving, hidden clues, dark secrets
  - Horror: Supernatural terrors, haunted places, survival
  - Romance: Love stories, emotional journeys, relationships
  - Adventure: Treasure hunts, exploration, daring escapades

- **Character Creation**: Design your unique protagonist
  - Custom name and class selection
  - Multiple personality traits (brave, wise, charming, clever, determined)
  - Genre-specific character classes
  - Dynamic character backgrounds

- **Dynamic Story Generation**: AI-powered narrative engine
  - Context-aware story chapters
  - Choice-driven plot development
  - Multiple story paths and outcomes
  - Rich, descriptive storytelling

### Interactive Elements
- **Meaningful Choices**: Every decision matters
  - 3+ choices per story segment
  - Consequences affect relationships and story progression
  - No "wrong" choices, just different paths

- **Character Relationships**: Build connections with NPCs
  - Relationship tracking (-100 to +100 scale)
  - Multiple relationship types (ally, rival, romantic, neutral)
  - Visual relationship dashboard
  - Interactions affect future story events

- **Achievement System**: Unlock special achievements
  - Story progression achievements
  - Relationship milestones
  - Special action rewards
  - Complete achievement gallery

### Technical Features
- **Auto-Save System**: Never lose your progress
  - Automatic progress saving after each choice
  - Multiple save slot support
  - Save management interface
  - Load any previous save

- **Responsive Design**: Play anywhere
  - Mobile-optimized interface
  - Tablet and desktop support
  - Smooth animations and transitions
  - Beautiful gradient designs

- **Immersive UI/UX**
  - Typewriter text effect for story content
  - Smooth fade and slide animations
  - Interactive hover states
  - Clean, modern game interface
  - Dark theme optimized for reading

---

## Technology Stack

### Frontend
- **React 18**: Modern UI library with hooks
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Utility-first styling
- **Vite**: Lightning-fast build tool
- **Lucide React**: Beautiful icon library

### Backend
- **Supabase**: Complete backend platform
  - PostgreSQL database
  - Real-time subscriptions
  - Row Level Security (RLS)
  - Authentication ready

### Architecture
- **Component-based**: Modular, reusable components
- **Context API**: Global state management
- **Custom Hooks**: Reusable logic patterns
- **TypeScript Types**: Full type safety

---

## Installation

### Prerequisites
- Node.js 18+ and npm
- Supabase account (free tier works)

### Setup Steps

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd storyforge
```

2. **Install dependencies**
```bash
npm install
```

3. **Configure Supabase**
   - Create a new Supabase project at [supabase.com](https://supabase.com)
   - The database schema is automatically set up
   - Your credentials are already in `.env`:
```env
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
```

4. **Run the development server**
```bash
npm run dev
```

5. **Open your browser**
   - Navigate to `http://localhost:5173`
   - Start your adventure!

---

## Project Structure

```
storyforge/
├── src/
│   ├── components/          # React components
│   │   ├── WelcomeScreen.tsx
│   │   ├── GenreSelection.tsx
│   │   ├── CharacterCreation.tsx
│   │   ├── StoryDisplay.tsx
│   │   ├── RelationshipPanel.tsx
│   │   ├── AchievementPanel.tsx
│   │   └── SavePanel.tsx
│   ├── context/             # React context
│   │   └── GameContext.tsx
│   ├── lib/                 # Utilities & logic
│   │   ├── supabase.ts
│   │   ├── database.ts
│   │   └── storyEngine.ts
│   ├── types/               # TypeScript types
│   │   └── game.ts
│   ├── App.tsx              # Main app component
│   ├── main.tsx             # Entry point
│   └── index.css            # Global styles
├── supabase/
│   └── migrations/          # Database migrations
├── package.json
├── vite.config.ts
├── tailwind.config.js
└── README.md
```

---

## Database Schema

### Tables

#### user_profiles
Stores player information
- `id`: UUID (primary key)
- `username`: Text
- `created_at`: Timestamp
- `last_played`: Timestamp

#### game_saves
Stores game progress
- `id`: UUID (primary key)
- `user_id`: UUID (foreign key)
- `save_slot`: Integer (1-3)
- `save_name`: Text
- `genre`: Text
- `character_name`: Text
- `character_traits`: JSONB
- `current_chapter`: Integer
- `story_state`: JSONB
- `created_at`: Timestamp
- `updated_at`: Timestamp

#### story_chapters
Stores generated story content
- `id`: UUID (primary key)
- `save_id`: UUID (foreign key)
- `chapter_number`: Integer
- `title`: Text
- `content`: Text
- `scene_type`: Text
- `location`: Text
- `created_at`: Timestamp

#### player_choices
Tracks player decisions
- `id`: UUID (primary key)
- `chapter_id`: UUID (foreign key)
- `choice_text`: Text
- `choice_index`: Integer
- `consequences`: JSONB
- `created_at`: Timestamp

#### character_relationships
Manages NPC relationships
- `id`: UUID (primary key)
- `save_id`: UUID (foreign key)
- `character_name`: Text
- `relationship_level`: Integer (-100 to 100)
- `relationship_type`: Text
- `first_met_chapter`: Integer
- `interactions`: Integer
- `updated_at`: Timestamp

#### achievements
Tracks unlocked achievements
- `id`: UUID (primary key)
- `user_id`: UUID (foreign key)
- `achievement_key`: Text
- `achievement_name`: Text
- `achievement_description`: Text
- `unlocked_at`: Timestamp

---

## Usage Guide

### Starting a New Game

1. **Welcome Screen**: Click "Start Your Adventure"
2. **Genre Selection**: Choose your preferred story genre
3. **Character Creation**:
   - Enter your character name
   - Select a class (varies by genre)
   - Choose up to 3 personality traits
4. **Begin Your Story**: Click "Begin Adventure"

### Playing the Game

1. **Read the Story**: Each chapter unfolds with typewriter effect
2. **Make Choices**: Select from 3+ options that shape your story
3. **Track Progress**: Monitor relationships and achievements
4. **Save Your Game**: Progress auto-saves after each choice

### Managing Saves

- **View Saves**: Click the save icon in the top bar
- **Load Save**: Select any previous save to continue
- **Delete Save**: Remove unwanted saves
- **Multiple Playthroughs**: Try different genres and choices

### Building Relationships

- **Meet NPCs**: Characters appear throughout your story
- **Make Choices**: Decisions affect relationship levels
- **View Relationships**: Click the users icon to see all connections
- **Relationship Types**: Relationships evolve (ally, rival, romantic, neutral)

### Unlocking Achievements

- **Story Milestones**: Complete chapters to earn achievements
- **Special Actions**: Discover hidden achievements
- **View Gallery**: Click the trophy icon to see all achievements

---

## Customization

### Adding New Genres

Edit `src/lib/storyEngine.ts`:
```typescript
// Add to NPCs object
fantasy: ['Your', 'NPC', 'Names'],

// Add to locations object
fantasy: ['Your', 'Location', 'Names'],

// Add genre templates in getChapterTemplates()
```

### Styling Changes

Edit `tailwind.config.js` for theme customization:
```javascript
theme: {
  extend: {
    colors: {
      // Your custom colors
    }
  }
}
```

### Custom Animations

Add to `src/index.css`:
```css
@keyframes yourAnimation {
  from { /* start state */ }
  to { /* end state */ }
}
```

---

## Performance Optimization

- **Lazy Loading**: Components load on demand
- **Optimized Rendering**: React.memo for heavy components
- **Efficient Database Queries**: Indexed columns for fast lookups
- **Debounced Auto-Save**: Prevents excessive database writes
- **Responsive Images**: Optimized for all device sizes

---

## Security

### Row Level Security (RLS)
All database tables use RLS policies:
- Users can only access their own data
- Authentication required for all operations
- Secure relationships between tables

### Best Practices
- Environment variables for secrets
- No sensitive data in client code
- Prepared statements prevent SQL injection
- HTTPS enforced in production

---

## Troubleshooting

### Common Issues

**Database Connection Errors**
- Verify Supabase credentials in `.env`
- Check Supabase project status
- Ensure migrations ran successfully

**Story Not Loading**
- Clear browser cache
- Check console for errors
- Verify save exists in database

**Slow Performance**
- Check network connection
- Reduce animation complexity
- Clear old save data

**Styling Issues**
- Run `npm run build` to rebuild
- Check Tailwind config
- Clear browser cache

---

## Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Guidelines
- Follow existing code style
- Add TypeScript types for new features
- Test thoroughly before submitting
- Update README for significant changes

---

## Roadmap

### Planned Features
- [ ] Voice narration option
- [ ] More genre varieties
- [ ] Multiplayer story mode
- [ ] Story export to PDF
- [ ] Custom story creation tools
- [ ] Mobile app versions
- [ ] Achievement sharing
- [ ] Story statistics dashboard
- [ ] AI-powered character portraits
- [ ] Music and sound effects
- [ ] Translation support

---

## License

### MIT License

Copyright (c) 2024 Achref Rhouma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Credits

### Created by Achref Rhouma

**StoryForge** is a passion project combining:
- Modern web development techniques
- Interactive storytelling principles
- Beautiful UI/UX design
- Scalable database architecture

### Technologies Used
- React & TypeScript
- Supabase & PostgreSQL
- Tailwind CSS
- Vite
- Lucide Icons

### Inspiration
Inspired by classic choose-your-own-adventure books and modern interactive fiction games, StoryForge aims to make interactive storytelling accessible and engaging for everyone.

---

## Support

### Get Help
- **Issues**: Report bugs via GitHub Issues
- **Questions**: Open a discussion on GitHub
- **Email**: Contact via achref@example.com

### Show Your Support
If you enjoy StoryForge:
- ⭐ Star the repository
- 🐛 Report bugs
- 💡 Suggest features
- 🔀 Contribute code
- 📢 Share with friends

---

## Acknowledgments

- Thanks to the React team for an amazing framework
- Supabase for making backend development simple
- Tailwind CSS for beautiful, fast styling
- The open-source community for inspiration

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

**Built with ❤️ by Achref Rhouma**

*Start your adventure today and forge your own story!*

---
id: tool-01283
type: tool
area: 库
status: active
tags: [协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: Revenge-Story-Video-Generator---Automated-YouTube-Content-Pipeline
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/redoanuzzaman/revenge-story-video-generator---automated-youtube-content-pipeline
created: 2026-07-18
updated: 2026-07-18
no: 1283
category: 二、网文 / 长篇 AI 写作系统 库
repo: REDOANUZZAMAN/Revenge-Story-Video-Generator---Automated-YouTube-Content-Pipeline
stars: 2
url: https://github.com/redoanuzzaman/revenge-story-video-generator---automated-youtube-content-pipeline
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 2bd4131e85584b2a
  - methods/最强写作方法论_全球最强综合版.md
---

# REDOANUZZAMAN/Revenge-Story-Video-Generator---Automated-YouTube-Content-Pipeline

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/redoanuzzaman/revenge-story-video-generator---automated-youtube-content-pipeline
- **Stars**：2
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：A comprehensive n8n workflow that scrapes Reddit revenge stories, uses AI to enhance and fictionalize them, generates professional narrated videos with custom avatars, and automatically uploads to YouTube. Perfect for creating engaging storytelling content at scale.
- **本地描述**：A comprehensive n8n workflow that scrapes Reddit revenge stories, uses AI to enhance and fictionalize them, generates professional narrated videos with custom avatars, and automatically uploads to YouTube. Perfect for creating engaging storytelling content at scale.
- **拉取时间**：2026-07-23 23:16:30

---

# 🎬 Revenge Story Video Generator - Automated YouTube Content Pipeline

A comprehensive n8n workflow that scrapes Reddit revenge stories, uses AI to enhance and fictionalize them, generates professional narrated videos with custom avatars, and automatically uploads to YouTube. Perfect for creating engaging storytelling content at scale.

![Status](https://img.shields.io/badge/status-active-success.svg)
![n8n](https://img.shields.io/badge/n8n-workflow-EA4B71?logo=n8n)
![Reddit](https://img.shields.io/badge/Reddit-FF4500?logo=reddit&logoColor=white)
![YouTube](https://img.shields.io/badge/YouTube-FF0000?logo=youtube&logoColor=white)

## ✨ Features

- **Reddit Integration** - Scrapes r/revengestories for top monthly content
- **AI Content Classification** - Filters stories vs. advice requests vs. rants
- **Story Enhancement** - Rewrites stories with proper narrative structure (3-act plot)
- **Character Generation** - Creates fictionalized personas from real stories
- **Multi-Language Support** - 8+ languages (English, Spanish, French, Chinese, etc.)
- **Text-to-Speech** - Gender-matched voice synthesis
- **Video Generation** - Custom avatar + background video + narration
- **Supabase Database** - Tracks story status through pipeline
- **YouTube Automation** - Auto-uploads finished videos
- **Duplicate Detection** - Prevents reprocessing same stories
- **Status Tracking** - queued → processing → created → uploaded

## 🔄 Workflow Overview

### Architecture

The workflow operates in **two main phases** and supports **two separate instances** (workflows 1 and 2 shown side-by-side in JSON):

### Phase 1: Story Collection & Filtering

```
Manual Trigger
     ↓
Get Stories from Reddit
  (r/revengestories top monthly)
     ↓
Split into Individual Posts
     ↓
Filter Out Videos
     ↓
Loop Through Each Post
     ↓
Set Fields (title, content, permalink, reddit_id)
     ↓
Check Supabase: Already Exists?
  ↓ (if new)
AI Classifier: Is it a Story?
  ├─→ Story → Save as "queued"
  ├─→ Ask for Advice → Skip
  └─→ Ranting → Skip
```

### Phase 2: Story Processing & Video Generation

```
Configuration Setup
  (language, voice, images, server URL)
     ↓
Setup Language Mapping
     ↓
Setup Character Sex
     ↓
Get Next Queued Story
     ↓
Is There a Story? (Decision)
  ↓ (yes)
AI: Create Character
  (name, age, location, sex)
     ↓
AI: Write Enhanced Story
  (3-act structure, 8th grade reading level)
     ↓
Cleanup Text (remove formatting)
     ↓
AI: Generate Title (<100 chars)
     ↓
Cleanup Title
     ↓
Voice Selection
  ├─→ Pre-selected? → Use configured voice
  └─→ Random → Fetch available voices → Match sex
     ↓
Set Final Voice
     ↓
Start Video Creation
  (POST to video generation server)
     ↓
Wait 10 seconds
     ↓
Check Video Status
     ↓
Switch (Status Check)
  ├─→ Processing → Wait again (loop)
  ├─→ Failed → Update status, exit
  └─→ Completed → Continue
     ↓
Setup Download URL
     ↓
Update Status: "created"
     ↓
Download Video
     ↓
Upload to YouTube
     ↓
Update Status: "uploaded"
```

## 🚀 Quick Start

### Prerequisites

- n8n instance (self-hosted or cloud)
- Supabase account (database)
- Video generation server (custom API)
- YouTube API credentials
- AI LLM access (Ollama, OpenAI, OpenRouter, etc.)
- Reddit (public API, no auth needed)

### Supabase Database Setup

```sql
-- Create revenge_stories table
CREATE TABLE revenge_stories (
  id SERIAL PRIMARY KEY,
  reddit_id TEXT UNIQUE NOT NULL,
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  permalink TEXT NOT NULL,
  status TEXT NOT NULL, -- 'queued', 'processing', 'created', 'uploaded', 'skipped', 'failed'
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Create index for status queries
CREATE INDEX idx_revenge_stories_status ON revenge_stories(status);
CREATE INDEX idx_revenge_stories_reddit_id ON revenge_stories(reddit_id);
```

### Video Generation Server

This workflow requires a **custom video generation API** with endpoints:

```
POST /api/videos
  Body: {
    text, person_image_url, person_name, 
    bg_video_url, voice
  }
  Returns: { video_id }

GET /api/videos/{video_id}/status
  Returns: { status: "processing" | "completed" | "failed" }

GET /api/videos/{video_id}
  Returns: video file (binary)

GET /api/languages
  Returns: { "en-us": [...voices], "es": [...voices], ... }
```

**Note**: The video generation server is not included. You'll need to build or use:
- [D-ID API](https://www.d-id.com/) for talking avatars
- [ElevenLabs](https://elevenlabs.io/) or similar for TTS
- Custom FFmpeg pipeline for video composition

### Workflow Installation

1. **Import Workflow**
   ```bash
   1. Download "revenge-story-workflow.json"
   2. In n8n: Import from File
   3. Upload JSON file
   ```

2. **Configure Settings**
   ```javascript
   // "Configuration for story writing" node
   {
     bg_video_url: "https://example.com/background.mp4",
     person_female_image_url: "https://example.com/female-avatar.png",
     person_male_image_url: "https://example.com/male-avatar.png",
     server_url: "YOUR_SERVER_URL", // Video generation API
     lang_code: "en-us", // or "es", "fr", "zh", etc.
     voice: "", // Leave empty for random, or specify
     sex: "" // Leave empty for random, or "male"/"female"
   }
   ```

3. **Add Credentials**
   - Supabase API key
   - YouTube OAuth (for uploads)
   - LLM provider (OpenAI, Ollama, etc.)

4. **Configure LLM Model**
   - Enable one AI model node (disable others)
   - Options: Ollama, OpenAI, OpenRouter, Google Gemini, Azure OpenAI, xAI Grok

5. **Test Phase 1** (Story Collection)
   - Run workflow once
   - Check Supabase for queued stories

6. **Test Phase 2** (Video Generation)
   - Ensure video server is running
   - Run workflow to process one story

## ⚙️ Configuration

### Language Support

```javascript
// Supported languages (in "Setup language" node)
const languages = {
  "en-us": "english",
  "en-gb": "english",
  "zh": "simplified chinese",
  "es": "spanish",
  "fr": "french",
  "it": "italian",
  "pt": "brazilian portugese",
  "hi": "hindi"
};
```

### Story Classification

```javascript
// AI Text Classifier categories
categories: [
  "story",           // Narrative revenge stories (queued)
  "ask_for_advice",  // Questions (skipped)
  "ranting"          // Complaints (skipped)
]
```

### Character Sex Logic

```javascript
// Automatic sex selection
sex = config.sex || 
      (lang_code === 'fr' ? 'female' : 
      ['male', 'female'].randomItem())

// French defaults to female for linguistic reasons
```

### Voice Selection

```javascript
// Pre-selected voice (fixed)
voice: "af_sky" // Use same voice for all videos

// Random voice (automatic)
voice: "" // Fetches available voices, matches character sex
// Example male: "am_adam", "am_michael"
// Example female: "af_sarah", "af_nicole"
```

### Video Assets

```javascript
// Background video requirements
- Format: MP4
- Duration: 5-15 minutes (looped as needed)
- Resolution: 1920x1080 or 1080x1920
- Content: Nature, gameplay, abstract visuals

// Avatar images requirements  
- Format: PNG with transparency preferred
- Size: 512x512 or 1024x1024
- Style: Consistent across male/female
- Background: Solid color or transparent
```

## 📁 Workflow Structure

```
Revenge Story Video Generator/
├── Phase 1: Story Collection
│   ├── Manual Trigger
│   ├── Get stories from Reddit (HTTP Request)
│   ├── Split Out (children array)
│   ├── Filter (no videos)
│   ├── Loop Over Items (batch processing)
│   ├── Set fields (extract data)
│   ├── Look up the id (Supabase check)
│   ├── Already exists? (If decision)
│   ├── Is it a story? (AI Text Classifier)
│   │   ├─→ Story: Save post (status: queued)
│   │   └─→ Other: Skip post (status: skipped)
│   └── Loop back
│
├── Phase 2: Video Generation
│   ├── Configuration for story writing
│   ├── Setup language (Code node)
│   ├── Setup sex of the main character
│   ├── Get the next story to process (Supabase)
│   ├── Is there a story to process? (If)
│   ├── Create character (AI Information Extractor)
│   ├── Write the story (AI LLM Chain)
│   ├── Cleanup text (Set node with regex)
│   ├── Create title (AI LLM Chain)
│   ├── Cleanup title (Set node)
│   ├── Is there a pre-selected voice? (If)
│   │   ├─→ Yes: Keep original value
│   │   └─→ No: HTTP Request → Set random voice
│   ├── Set the final voice
│   ├── Start creating the video (HTTP POST)
│   ├── Wait (10 seconds)
│   ├── Check video status (HTTP GET)
│   ├── Switch (status routing)
│   │   ├─→ processing: Wait again (loop)
│   │   ├─→ failed: Set status to failed
│   │   └─→ completed: Continue
│   ├── Setup the download url
│   ├── Set status to created (Supabase)
│   ├── Download the video (HTTP GET)
│   ├── Share on YouTube (YouTube node)
│   └── Set status to uploaded (Supabase)
│
└── AI Model Selection (choose one)
    ├── Ollama Model (local)
    ├── OpenAI Chat Model
    ├── OpenRouter Chat Model
    ├── Google Gemini Chat Model
    ├── Azure OpenAI Chat Model
    └── xAI Grok Chat Model
```

**Total Nodes**: 150+ (dual workflow instances)

## 🎯 How It Works

### Phase 1: Story Collection (Run Daily/Weekly)

1. **Fetch from Reddit**
   - API: `https://www.reddit.com/r/revengestories/top.json?t=month&limit=100`
   - Gets top 100 posts from last month
   - No authentication required (public data)

2. **Filter Content**
   - Removes video posts (is_video = false)
   - Extracts: title, selftext (content), permalink, id

3. **Check Duplicates**
   - Queries Supabase by reddit_id
   - Skips if already processed

4. **AI Classification**
   - Analyzes title + content
   - Categorizes as story/advice/rant
   - Only stories marked as "queued"

5. **Save to Database**
   - Status: "queued" (ready for processing)
   - Status: "skipped" (not a story)

### Phase 2: Video Generation (Run Continuously)

6. **Retrieve Queued Story**
   - Gets one story with status="queued"
   - Updates to prevent duplicate processing

7. **Create Character**
   - AI generates: name, age, location, sex
   - Fictionalized (doesn't use real details)
   - Matches language/culture (e.g., French names for French)

8. **Write Enhanced Story**
   - AI follows 3-act structure:
     - **Act 1**: Setup character and problem
     - **Act 2**: Attempts fail, stakes rise
     - **Act 3**: Final attempt, resolution, twist
   - 8th grade reading level
   - First person narrative
   - No acronyms (spelled out for TTS)
   - Continuous text (no paragraphs for narration)

9. **Generate Title**
   - AI creates <100 character title
   - Attention-grabbing and descriptive
   - Matches story language

10. **Select Voice**
    - If pre-configured: Use specified voice
    - If random: Fetch available voices from API
    - Filter by character sex (male/female)
    - Randomly select from matching voices

11. **Start Video Creation**
    - POST request to video generation server
    - Sends: text, avatar, name, background, voice
    - Receives: video_id

12. **Poll for Completion**
    - Wait 10 seconds
    - Check status endpoint
    - Loop until "completed" or "failed"

13. **Download Video**
    - GET video file from server
    - Binary data stored in n8n

14. **Upload to YouTube**
    - Uses YouTube Data API v3
    - Title from AI-generated title
    - Category: Entertainment (24)
    - Region: Configurable (default: HU)

15. **Update Status**
    - Marks as "uploaded" in Supabase
    - Story removed from queue

## 🎨 Customization Examples

### Change Reddit Source

```javascript
// Get stories from Reddit node
url: "https://www.reddit.com/r/revengestories/top.json?t=month&limit=100"

// Options:
t=day     // Last 24 hours
t=week    // Last week
t=month   // Last month (default)
t=year    // Last year
t=all     // All time

// Or change subreddit:
url: "https://www.reddit.com/r/ProRevenge/top.json?t=month&limit=100"
url: "https://www.reddit.com/r/pettyrevenge/top.json?t=month&limit=100"
```

### Adjust Story Length

```javascript
// Write the story node - modify prompt
"7. The story should be very long"
→ "7. The story should be 5-7 minutes when spoken aloud"
→ "7. The story should be concise, under 3 minutes"
```

### Different Narrative Style

```javascript
// Write the story prompt
"3. The story should be told in first person"
→ "3. The story should be told in third person"
→ "3. The story should be told as a news report"
→ "3. The story should be told with dramatic narration"
```

### Custom YouTube Settings

```javascript
// Share on YouTube node
{
  title: "{{ title }}",
  regionCode: "HU",      // Change to "US", "GB", "DE", etc.
  categoryId: "24",      // Entertainment
  // Other options:
  // 22: People & Blogs
  // 23: Comedy
  // 25: News & Politics
  
  options: {
    description: "...",   // Add description
    tags: [revenge, story"], // Add tags]
    privacyStatus: "public" // or "unlisted", "private"
  }
}
```

### Multiple AI Models

```javascript
// Enable different models for different tasks
// Story classification: Fast model (GPT-4o-mini)
// Story writing: Quality model (GPT-4, Claude Opus)
// Title generation: Fast model (GPT-4o-mini)

// Connect different model nodes to different AI tasks
```

## 🛠️ Node Breakdown

| Category | Node Type | Count | Purpose |
|----------|-----------|-------|---------|
| **Reddit Collection** | HTTP Request | 2 | Fetch posts (2 workflow instances) |
| | Split Out | 2 | Separate posts |
| | Filter | 2 | Remove videos |
| | Split In Batches | 2 | Loop processing |
| | Set | 2 | Extract fields |
| **Database** | Supabase Get | 4 | Check duplicates, get queued |
| | Supabase Insert | 4 | Save/skip posts |
| | Supabase Update | 6 | Status updates |
| **AI Processing** | Text Classifier | 2 | Story classification |
| | Information Extractor | 2 | Character creation |
| | Chain LLM | 4 | Story writing, titles |
| | LLM Model | 12 | Various model options |
| **Logic** | If | 8 | Decision points |
| | Switch | 2 | Status routing |
| | Wait | 2 | Polling delays |
| **Video** | HTTP Request | 8 | API calls (create, status, download) |
| | YouTube | 2 | Upload videos |
| | Set | 20+ | Data transformation |
| | Code | 2 | Language mapping |
| **Other** | No Op | 4 | Terminal nodes |
| | Manual Trigger | 1 | Workflow start |
| | Sticky Note | 13 | Documentation |

**Total Active Nodes**: ~80 per workflow instance × 2 = 160

## 🔧 Troubleshooting

### No Stories Retrieved from Reddit

```javascript
// Check Reddit API
1. Test URL in browser
2. Verify subreddit exists: r/revengestories
3. Try different time period (t=week instead of month)
4. Check if subreddit has posts

// Common issues:
- Subreddit banned/private
- No posts in time period
- Reddit API rate limiting (unlikely with no auth)
```

### AI Classification Not Working

```javascript
// Text Classifier node
1. Verify LLM model is connected
2. Check model credentials
3. Test with simpler categories:
   - "story"
   - "not_story"

// If using Ollama
1. Ensure Ollama is running: ollama list
2. Check model is pulled: ollama pull qwen3:32b
3. Verify n8n can reach Ollama host
```

### Character Creation Fails

```javascript
// Information Extractor node
1. Check story content isn't empty
2. Verify LLM model connection
3. Test with simpler attributes (just name + age)

// Language mismatch
- Ensure lang_code matches language mapping
- Check if LLM supports target language
```

### Story Writing Produces Errors

```javascript
// Common issues
1. Story too long for token limit
   - Split into chunks
   - Use model with larger context (100K+)
   
2. Formatting issues
   - Check cleanup regex in "Cleanup text"
   - Verify .replace() patterns work
   
3. LLM refuses content
   - Some stories may violate content policies
   - Try different LLM provider
   - Adjust prompt to emphasize "fictionalized"
```

### Video Generation Server Errors

```javascript
// Start creating the video node
1. Verify server_url is accessible
2. Check POST body format matches API
3. Test API manually with curl/Postman

// Status never completes
1. Check server logs for errors
2. Verify TTS voice is available
3. Check image URLs are accessible
4. Ensure background video exists

// Recommended timeout: 5-10 minutes max
```

### Video Download Fails

```javascript
// HTTP Request node
1. Check download URL format
2. Verify video_id is correct
3. Ensure server returns binary data
4. Check n8n binary data handling

// Large files
- Videos may be 50-200MB
- Ensure n8n has sufficient memory
- Check server bandwidth
```

### YouTube Upload Errors

```javascript
// Common OAuth issues
1. Re-authenticate YouTube credentials
2. Check OAuth scopes include:
   - youtube.upload
   - youtube.force-ssl
3. Verify API quota not exceeded (10,000 units/day)

// Upload fails
1. Check video format (MP4 required)
2. Verify title <100 characters
3. Check category ID is valid
4. Test with smaller video first
```

### Supabase Connection Issues

```javascript
// Database errors
1. Verify API key is correct (service_role)
2. Check table name: "revenge_stories"
3. Verify schema matches
4. Check RLS policies (disable for testing)

// Duplicate key errors
- reddit_id must be unique
- Check if story already exists
- Verify "Already exists?" node works
```

### Workflow Runs But Doesn't Process

```javascript
// Common causes
1. No queued stories in database
   - Run Phase 1 first
   - Check status="queued" count

2. If node skips execution
   - Check "Is there a story to process?"
   - Verify Supabase returns data

3. Loops infinitely
   - Check Wait time isn't too short
   - Verify Switch node routing
```

## 💡 Enhancement Ideas

### Immediate Improvements
- [ ] Add thumbnail generation
- [ ] Schedule uploads (not immediate)
- [ ] Add video descriptions with links
- [ ] Create playlists automatically
- [ ] Track video performance metrics
- [ ] A/B test different titles

### Advanced Features
- [ ] Multiple Reddit sources simultaneously
- [ ] Story quality scoring
- [ ] Audience retention analysis
- [ ] Automatic re-uploads (delisted videos)
- [ ] Multi-platform posting (TikTok, Instagram)
- [ ] Comments moderation automation
- [ ] Monetization tracking

### AI Enhancements
- [ ] Generate custom background images
- [ ] Create multiple video versions
- [ ] Optimize story length for retention
- [ ] Auto-generate hashtags
- [ ] Sentiment analysis for story selection
- [ ] Voice cloning for consistency
- [ ] Music soundtrack generation

### Production Features
- [ ] Error notification system
- [ ] Detailed logging/analytics
- [ ] Retry failed videos
- [ ] Priority queue system
- [ ] Cost tracking per video
- [ ] Rate limiting for APIs
- [ ] Graceful degradation

## 📊 Performance Metrics

### Execution Time (Per Story)
- **Story collection**: 10-30 seconds (100 stories)
- **AI classification**: 2-5 seconds per story
- **Character creation**: 5-10 seconds
- **Story writing**: 30-60 seconds (depends on length)
- **Title generation**: 5-10 seconds
- **Video creation**: 5-15 minutes (server-dependent)
- **YouTube upload**: 1-5 minutes (size-dependent)

**Total per video**: 10-20 minutes average

### API Costs (Approximate)
- **Reddit API**: Free
- **Supabase**: Free tier (500MB storage)
- **AI LLM calls**: $0.10-0.50 per story (varies by model)
  - Classification: $0.01
  - Character: $0.02-0.05
  - Story writing: $0.05-0.30
  - Title: $0.02
- **Video generation**: Varies by provider
  - D-ID: $0.30-0.50 per minute
  - ElevenLabs TTS: $0.30 per 1000 chars
- **YouTube upload**: Free

**Total per video**: $1-5 depending on providers

### Resource Requirements
- **n8n**: Moderate (100-500MB RAM per execution)
- **Database**: ~5-10KB per story
- **Storage**: 50-200MB per generated video
- **Bandwidth**: 100-500MB per video (download + upload)

## 🔒 Security & Best Practices

- **API Keys**: Store in n8n credentials only
- **Supabase RLS**: Enable for production
- **Reddit**: Respect rate limits (no auth = generous)
- **Content Moderation**: Review stories before posting
- **YouTube TOS**: Ensure compliance with policies
- **Copyright**: Stories are user-generated (fair use applies)
- **Privacy**: Fictionalize names and locations
- **Content Policy**: Filter inappropriate stories

## 📝 Credentials Setup

### Supabase

```
1. Create project at supabase.com
2. Create "revenge_stories" table (schema above)
3. Get API URL and service_role key
4. Add to n8n Supabase credentials
```

### YouTube API

```
1. Create project at console.cloud.google.com
2. Enable YouTube Data API v3
3. Create OAuth credentials
4. Add redirect URI (n8n webhook URL)
5. Configure OAuth consent screen
6. Add to n8n YouTube credentials
7. Authorize account
```

### LLM Provider (Example: OpenAI)

```
1. Get API key from platform.openai.com
2. Add to n8n OpenAI credentials
3. Select model: gpt-4o-mini (fast) or gpt-4 (quality)
```

### Video Generation Server

```
Custom API - build your own or use services:
- D-ID (talking avatars)
- ElevenLabs (TTS)
- FFmpeg (video composition)
- Hosting: VPS, AWS, GCP, etc.
```

## 📖 Additional Resources

- [Reddit API Docs](https://www.reddit.com/dev/api/)
- [YouTube Data API](https://developers.google.com/youtube/v3)
- [Supabase Documentation](https://supabase.com/docs)
- [n8n LangChain Nodes](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain/)
- [D-ID API](https://docs.d-id.com/)
- [ElevenLabs API](https://elevenlabs.io/docs)

## 🎬 Example Output

**Input** (Reddit post):
```
Title: "My coworker kept stealing my lunch, so I got revenge"
Content: [500 words about lunch thief]
```

**AI Character**:
```
Name: Marcus Chen
Age: 32
Location: Seattle, Washington
Sex: Male
```

**AI Enhanced Story** (excerpt):
```
"I'm Marcus, and I'm thirty-two years old. I work at a tech 
company in Seattle where I thought I had found my dream job. 
For three years, everything was perfect until Derek joined 
our team. At first, he seemed nice enough, but then strange 
things started happening..."

[3-4 minute story continues with 3-act structure]
```

**Generated Video**:
- Male avatar speaking the narration
- Background: Subway Surfers gameplay
- Voice: Natural TTS matching character
- Duration: 4 minutes 23 seconds

**YouTube Upload**:
- Title: "Coworker Kept Stealing My Lunch Until I Got Perfect Revenge"
- Category: Entertainment
- Status: Public
- Region: Worldwide

## 📄 License

This workflow is open source and available under the [MIT License](https://github.com/REDOANUZZAMAN/Revenge-Story-Video-Generator---Automated-YouTube-Content-Pipeline/blob/main/LICENSE).

## 🤝 Contributing

Contributions welcome! Focus areas:

- Video generation alternatives
- Additional Reddit sources
- Better story filtering
- Performance optimizations
- Multi-platform distribution

1. Fork repository
2. Create feature branch (`git checkout -b feature/TikTokIntegration`)
3. Commit changes (`git commit -m 'Add TikTok upload'`)
4. Push to branch (`git push origin feature/TikTokIntegration`)
5. Open Pull Request

## 👨‍💻 Author

**Redoanuzzaman**
- GitHub: [@REDOANUZZAMAN](https://github.com/REDOANUZZAMAN)
- Email: redoanuzzaman707@gmail.com
- Website: [redoan.dev](https://redoan.dev)

## 🙏 Acknowledgments

- Reddit for public API access
- n8n community for workflow automation
- OpenAI/Anthropic for LLM technology
- YouTube for content platform
- r/revengestories community

## 💖 Show Your Support

Give a ⭐️ if this workflow helps your content creation!

## 🎯 Use Cases

- **YouTube Channels**: Automated story content
- **Podcast**: Text-to-speech story narration
- **Social Media**: Short-form story videos
- **Education**: Narrative structure examples
- **Research**: AI storytelling capabilities
- **Entertainment**: Binge-worthy content series

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

Made with 🎬 and AI storytelling

**Last Updated:** October 2025

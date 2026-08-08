---
id: tool-00311
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: ZTagExpand
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/theholyonez/ztagexpand
created: 2026-07-18
updated: 2026-07-18
no: 311
category: 二、网文 / 长篇 AI 写作系统 库
repo: TheHolyOneZ/ZTagExpand
stars: 1
url: https://github.com/theholyonez/ztagexpand
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: d377a23cffd7ae9d
  - methods/最强写作方法论_全球最强综合版.md
---

# TheHolyOneZ/ZTagExpand

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/theholyonez/ztagexpand
- **Stars**：1
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：ZTagExpand is a sophisticated Discord bot cog that allows users to create AI-expandable tags. These tags use short prompts that are dynamically expanded into rich, context-aware content using Google's Gemini AI. Perfect for roleplay servers, creative writing communities, and any Discord server that needs dynamic, AI-generated content.
- **本地描述**：ZTagExpand is a sophisticated Discord bot cog that allows users to create AI-expandable tags. These tags use short prompts that are dynamically expanded into rich, context-aware content using Google's Gemini AI. Perfect for roleplay servers, creative writing communities, and any Discord server that needs dynamic, AI-generated content.
- **拉取时间**：2026-07-23 22:48:07

---

# ZTagExpand - AI Tag Expansion System

**Advanced AI-Powered Tag System for Discord**  
Created by **TheHolyOneZ** | Powered by **Google Gemini AI**


> 💡 **Built for the Zygnal Ecosystem — to download and use this extension, you must be part of the Zygnal Ecosystem.**  
> This extension (cog) is part of the **Zygnal Ecosystem** and is only available through its supported platforms.  
> You can use it with:  
> - The **[Discord Bot Framework](https://github.com/TheHolyOneZ/discord-bot-framework)** — ideal for developers who want full control and flexibility *(includes an integrated extension marketplace)*, or  
> - The **[ZygnalBot](https://zygnalbot.de)** — a prebuilt, plug-and-play Discord bot *(also includes an integrated extension marketplace)*.  
>
> Browse and install extensions at [zygnalbot.com/extension](https://zygnalbot.com/extension).  
> For help or community discussions, join us on Discord: [discord.gg/sgZnXca5ts](https://discord.gg/sgZnXca5ts)

---

## 📜 License

This software is released under a custom proprietary license. The full license text is located at the top of the source file. **All rights reserved.** Unauthorized modification, distribution, or removal of attribution is strictly prohibited.

---

## 🌟 Overview

ZTagExpand is a sophisticated Discord bot cog that allows users to create AI-expandable tags. These tags use short prompts that are dynamically expanded into rich, context-aware content using Google's Gemini AI. Perfect for roleplay servers, creative writing communities, and any Discord server that needs dynamic, AI-generated content.

---

## ✨ Key Features

### 🎯 Core Functionality
- **AI-Powered Tag Expansion**: Short prompts expand into detailed, contextual content
- **Dynamic Variables**: Use variables like `{user}`, `{server}`, `{time}`, `{date}`, and `{random:options}` in your tags
- **Multiple Style Presets**: Choose from narrative, roleplay, friendly, corporate, dark, anime, fantasy, and sci-fi writing styles
- **Customizable Output Length**: Short, medium, or long AI-generated responses
- **Public & Private Tags**: Control who can see and use your tags
- **Tag Categories**: Organize tags into categories (general, roleplay, fun, utility, creative, etc.)
- **Tag Ownership & Co-Ownership**: Share tag management with other users
- **Per-Tag Cooldowns**: Set individual cooldown timers for specific tags

### 🔒 Security & Data Management
- **Fernet 256-bit Encryption**: API keys are encrypted at rest using industry-standard encryption
- **Per-Guild Isolation**: Each server has completely isolated data storage
- **Automatic Backups**: Daily encrypted backups with retention management
- **Audit Logging**: Track all tag creation, modification, and deletion events
- **Path Traversal Protection**: Built-in security against file system attacks
- **Atomic File Operations**: Prevents data corruption during saves

### 📊 Advanced Features
- **Tag Version History**: View and revert to previous versions of any tag
- **Favorites System**: Mark frequently-used tags for quick access
- **Tag Search**: Find tags by name or prompt content
- **Usage Statistics**: Track tag usage, popular tags, and creator leaderboards
- **Scheduled Tag Posting**: Automatically post tags at intervals
- **Webhook Integration**: Send tag events to external services
- **Import/Export**: Bulk import and export tags as JSON files
- **Bulk Operations**: Mass delete, transfer ownership, or change visibility

### ⚙️ Administrative Controls
- **Role-Based Permissions**: Separate permissions for creators, viewers, editors, and cooldown bypass
- **Quota Management**: Limit tags per user and daily usage limits
- **Guild-Wide Token Limits**: Control AI API usage per server
- **Global & Role Cooldowns**: Flexible cooldown system with role-based exceptions
- **NSFW Content Controls**: Enable or disable mature content
- **Custom Style Presets**: Create server-specific writing styles
- **Interactive Admin Panel**: Easy-to-use tabbed interface for all settings

---

## 🚀 Getting Started

### Prerequisites
- A Google Gemini API key (obtain from Google AI Studio)
- Administrator permissions on your Discord server
- The bot must be invited with appropriate permissions

### Initial Setup

1. **Set API Key**  
   Run `/ztag_admin` and navigate to the API tab. Click "Set API Key" and enter your Gemini API key. It will be encrypted and securely stored.

2. **Configure Permissions** (Optional)  
   By default, all users can create and use tags. Use the Permissions tab in `/ztag_admin` to restrict access to specific roles.

3. **Customize Settings** (Optional)  
   Adjust default styles, output lengths, cooldowns, and other settings via the admin panel.

---

## 📖 User Commands

### `/tag add` - Create a New Tag
Create an AI-expandable tag with a custom prompt.

**Parameters:**
- `name` (required): Alphanumeric tag name (max 32 characters)
- `prompt` (required): Short AI prompt to expand (max 500 characters)
- `public` (optional): Make tag visible to everyone (default: False)
- `category` (optional): Organize into categories (default: general)
- `cooldown` (optional): Custom cooldown in seconds
- `context` (optional): Additional context with variables

**Example:**
```
/tag add name:greeting prompt:"Welcome a new member warmly" public:True category:utility
```

### `/tag use` - Expand a Tag
Generate AI content from a tag.

**Parameters:**
- `tag` (required): Tag name to expand (autocomplete available)
- `style` (optional): Override default style preset
- `length` (optional): Override output length (short/medium/long)

**Example:**
```
/tag use tag:greeting style:friendly length:medium
```

### `/tag list` - View Available Tags
Browse all tags you have access to, organized by ownership and favorites.

**Parameters:**
- `show_all` (optional): Admin-only, show all tags including private
- `category` (optional): Filter by category

### `/tag info` - Tag Details
View detailed information about a specific tag including owner, usage stats, category, and cooldown.

**Parameters:**
- `name` (required): Tag name to inspect

### `/tag edit` - Modify Your Tag
Edit prompt, visibility, category, cooldown, or context.

**Parameters:**
- `name` (required): Tag to edit
- `new_prompt` (optional): Update the prompt
- `public` (optional): Change visibility
- `category` (optional): Change category
- `cooldown` (optional): Update cooldown
- `context` (optional): Update context variables

### `/tag remove` - Delete a Tag
Permanently delete a tag you own or co-own.

**Parameters:**
- `name` (required): Tag to delete

### `/tag addowner` - Add Co-Owner
Grant another user co-ownership of your tag.

**Parameters:**
- `name` (required): Your tag
- `user` (required): User to add as co-owner

### `/tag favorite` - Add to Favorites
Mark a tag as favorite for quick access in autocomplete.

**Parameters:**
- `name` (required): Tag to favorite

### `/tag unfavorite` - Remove from Favorites
Remove a tag from your favorites list.

**Parameters:**
- `name` (required): Tag to unfavorite

### `/tag search` - Search Tags
Find tags by searching names and prompts.

**Parameters:**
- `query` (required): Search term

### `/tag history` - View Edit History
See previous versions of a tag you own or co-own.

**Parameters:**
- `name` (required): Tag name

### `/tag revert` - Restore Previous Version
Revert a tag to an earlier version.

**Parameters:**
- `name` (required): Tag name
- `version` (required): Version number (1 = most recent)

### `/tag schedule` - Auto-Post Tags
Schedule a tag to automatically post in a channel.

**Parameters:**
- `tag` (required): Tag to schedule
- `channel` (required): Channel to post in
- `interval` (required): Minutes between posts (0 for one-time)
- `start_time` (optional): When to start (HH:MM format)

**Note:** Administrator permission required.

### `/tag export` - Export Tags
Export all server tags to a JSON file for backup or migration.

**Note:** Administrator permission required.

### `/tag import` - Import Tags
Import tags from a JSON export file.

**Parameters:**
- `file` (required): JSON file from export
- `conflict_mode` (required): How to handle existing tags (skip/overwrite/rename)

**Note:** Administrator permission required.

### `/tag variables` - View Available Variables
Display all variables you can use in tag prompts and context.

---

## 🎛️ Admin Commands

### `/ztag_admin` - Administration Panel
Opens an interactive administration panel with multiple tabs:

**Tabs:**
1. **🏠 Main**: Overview of server statistics and quick status
2. **🔑 API**: Manage Gemini API key and encryption
3. **👥 Permissions**: Configure role-based access control
4. **⏱️ Cooldowns**: Set global and role-specific cooldowns
5. **🧩 Presets**: Manage AI writing style presets
6. **⚙️ Settings**: Toggle features and set defaults
7. **📊 Quotas**: Manage usage limits per user and guild
8. **📈 Stats**: View detailed usage analytics

### `/tag_bulk_delete` - Mass Delete by Category
Delete all tags in a specific category at once.

**Parameters:**
- `category` (required): Category to delete

**Note:** Administrator permission required.

### `/tag_bulk_transfer` - Transfer Ownership
Transfer all tags from one user to another.

**Parameters:**
- `old_owner` (required): Current owner
- `new_owner` (required): New owner

**Note:** Administrator permission required.

### `/tag_bulk_publicity` - Bulk Visibility Change
Change all tags in a category to public or private.

**Parameters:**
- `category` (required): Category to modify
- `public` (required): True for public, False for private

**Note:** Administrator permission required.

---

## 🔧 Variables System

Variables are replaced when a tag is used, allowing for dynamic, context-aware content.

### Available Variables

| Variable | Description | Example Output |
|----------|-------------|----------------|
| `{user}` | User's display name | "JohnDoe" |
| `{server}` | Server/guild name | "My Cool Server" |
| `{time}` | Current time (12h) | "3:45 PM" |
| `{date}` | Current date | "November 23, 2025" |
| `{random:a,b,c}` | Random choice | One of: a, b, or c |

### Usage Example

**Prompt:**
```
A hero from {server} named {user} discovers a {random:sword,shield,amulet} at {time}
```

**Expands to:**
```
A hero from My Cool Server named JohnDoe discovers a sword at 3:45 PM
```

---

## 🎨 Style Presets

Style presets control how the AI writes. Default presets include:

- **Narrative**: Vivid storytelling with descriptive language
- **RP (Roleplay)**: Immersive character perspective
- **Friendly**: Casual conversational tone
- **Corporate**: Professional business writing
- **Dark**: Atmospheric and mysterious
- **Anime**: Dramatic anime narrator style
- **Fantasy**: Epic fantasy storytelling
- **Sci-Fi**: Futuristic science fiction tone

Administrators can add custom presets via `/ztag_admin` → Presets tab.

---

## 📊 Permission System

### Permission Types

1. **Creator Roles**: Can create new tags
2. **Viewer Roles**: Can view and use tags
3. **Editor Roles**: Can edit any tag
4. **Cooldown Bypass Roles**: Ignore all cooldowns

**Default Behavior**: If no roles are set for a permission type, everyone is allowed (except cooldown bypass, which defaults to none).

**Admin Override**: Users with Administrator permission bypass all restrictions.

---

## ⏱️ Cooldown System

### Types of Cooldowns

1. **Global Cooldown**: Applies to all users for all tag uses
2. **Role Cooldowns**: Different cooldowns for different roles
3. **Per-Tag Cooldowns**: Individual tags can have custom cooldowns
4. **Cooldown Bypass**: Specific roles can ignore all cooldowns

**Priority**: Lower cooldowns take priority when a user has multiple roles.

---

## 📈 Statistics & Analytics

The system tracks:
- Total tags created
- Total expansions generated
- Most popular tags
- Top creators leaderboard
- Daily usage patterns
- Category distribution
- Recent activity logs

Access statistics via `/ztag_admin` → Stats tab.

---

## 💾 Data Management

### Automatic Backups
- Run every 24 hours per server
- Encrypted with Fernet encryption
- Retains last 15 backups
- Automatically purges old backups

### Version Control
- Last 5 versions saved per tag
- Can view and revert to previous versions
- Timestamp tracking for all changes

### Data Storage Structure
```
data/ztagexpand/
├── [guild_id]/
│   ├── settings.json          # Server configuration
│   ├── tags.json              # All tags
│   ├── statistics.json        # Usage analytics
│   ├── audit.log              # Action history
│   ├── schedules.json         # Scheduled posts
│   ├── favorites_[user].json  # User favorites
│   ├── quotas_[user].json     # User quotas
│   ├── backups/               # Encrypted backups
│   ├── versions/              # Tag version history
│   ├── secure/                # Encryption keys
│   └── security/              # API keys (.env)
```

---

## 🔔 Webhook Integration

Send tag events to external services (Discord webhooks, logging systems, etc.).

**Tracked Events:**
- Tag creation
- Tag usage
- Tag deletion
- Tag modification

**Setup**: Use `/ztag_admin` → Settings tab → "Set Webhook URL"

**Webhook Format**: Discord-compatible embeds with event details.

---

## 🛡️ NSFW Content Controls

Administrators can toggle NSFW tag creation via `/ztag_admin` → Settings → "Toggle NSFW".

**When Disabled:**
- Blocks tags with explicit keywords
- Prevents creation of mature content
- AI is instructed to refuse inappropriate prompts

**When Enabled:**
- Users can create any content
- Server responsibility for moderation

---

## 📦 Import/Export System

### Exporting Tags
1. Run `/tag export`
2. Receive JSON file with all server tags
3. Save for backup or migration

### Importing Tags
1. Run `/tag import`
2. Attach JSON file from export
3. Choose conflict resolution:
   - **Skip**: Don't import existing tags
   - **Overwrite**: Replace existing tags
   - **Rename**: Add suffix to imported tags

---

## 🎯 Quota System

Control resource usage with configurable limits:

### User Quotas
- **Max Tags per User**: Limit total tags a user can create
- **Max Daily Uses**: Limit tag expansions per user per day

### Guild Quotas
- **Max AI Tokens per Day**: Limit total API usage for the entire server

**Reset**: Daily quotas reset at midnight UTC.

---

## 🔍 Autocomplete Features

Many commands feature smart autocomplete:
- **Tag names**: Shows favorites first, then owned tags, then public tags
- **Categories**: Suggests configured categories
- **Style presets**: Lists available writing styles
- **Variables**: Suggests variable syntax with descriptions

---

## 💡 Best Practices

### For Users
1. **Use descriptive names**: Make tags easy to find and remember
2. **Keep prompts concise**: AI works best with clear, focused prompts
3. **Utilize variables**: Make tags dynamic and reusable
4. **Organize with categories**: Keep tags organized for easy discovery
5. **Favorite frequently-used tags**: Quick access via autocomplete

### For Administrators
1. **Set appropriate cooldowns**: Prevent spam without hindering legitimate use
2. **Configure role permissions**: Control who can create vs. use tags
3. **Monitor statistics**: Track usage patterns and adjust limits
4. **Regular backups**: Use export feature for additional backups
5. **Set reasonable quotas**: Balance resource usage with user experience
6. **Review audit logs**: Track who's creating and modifying tags

---

## ❓ Troubleshooting

### API Key Issues
- **Error: "API Key Not Configured"**: Set key via `/ztag_admin` → API tab
- **Error: "API Error (401)"**: Invalid API key, check Google AI Studio
- **Error: "API Error (429)"**: Rate limit exceeded, wait or upgrade API plan

### Permission Issues
- Ensure bot has proper Discord permissions (Send Messages, Embed Links)
- Check role-based permissions in admin panel
- Verify user has required roles for the action

### Tag Not Appearing
- Check if tag is private and you're not the owner
- Verify tag hasn't been deleted
- Use `/tag search` to locate tags

### Cooldown Issues
- Check global cooldown setting
- Verify role-based cooldowns
- Check per-tag cooldown settings
- Consider adding cooldown bypass role

---

## 🆘 Support

For issues, questions, or feature requests related to ZTagExpand:
- Visit: **zygnalbot.com**
- Contact: **TheHolyOneZ** via official channels

---

## 🙏 Credits

- **Created by**: TheHolyOneZ (TheZ)
- **Powered by**: Google Gemini AI
- **Part of**: Zygnalbot Extension Ecosystem

---

## ⚖️ Legal

This software is proprietary and protected by copyright. See the full license at the top of the source file. Unauthorized use, modification, or distribution is prohibited.

**Remember**: When using Gemini AI, you are subject to Google's terms of service and usage policies.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

**ZTagExpand** - Transform simple tags into rich, AI-powered content. 🚀

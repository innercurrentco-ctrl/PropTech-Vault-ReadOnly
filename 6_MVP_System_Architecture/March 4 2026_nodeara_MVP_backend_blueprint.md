
# Nodeara Backend Technical Blueprint

## 1. System Vision
Nodeara is a video-first real estate intelligence platform where video consumption generates intent signals that power listing recommendations.

Flow:
Video → Intent Signals → Recommendation Engine → Listings

## 2. Core Backend Stack
Framework: NestJS
Language: TypeScript
Database (future): PostgreSQL
Caching: Redis
ORM: Prisma
Storage: Cloudflare R2
Containerization: Docker

## 3. Modular Architecture
NestJS uses modules to organize backend systems.

Modules:
events
videos
surveys
intent
listings

Each module contains:
- controller
- service
- module
- dto

## 4. Project Folder Structure

src/

app.module.ts
main.ts

events/
videos/
surveys/
intent/

listings/
  dto/
    create-listing.dto.ts
  listings.controller.ts
  listings.service.ts
  listings.module.ts

## 5. Listings API

GET /listings
GET /listings/:id
POST /listings
DELETE /listings/:id

## 6. Data Model Concept

Listing
- id
- title
- address
- price
- coverImageUrl
- createdAt

Video
- id
- listingId
- url
- duration

IntentSignal
- id
- userId
- videoId
- intentType
- confidenceScore

## 7. Listing → Video Relationship

One listing can contain multiple videos.

Listing
   ↓
Video 1
Video 2
Video 3

## 8. Intent Signal Pipeline

User watches video
↓
Playback analytics recorded
↓
Intent signal generated
↓
Stored in database
↓
Recommendation engine updates

## 9. Recommendation Engine Concept

Signals used:
watch time
completion rate
replays
location preference

Output:
recommended listings
trending listings
similar listings

## 10. Scalability Plan

Phase 1
Single NestJS server

Phase 2
PostgreSQL database
Redis caching

Phase 3
Microservices
Recommendation service
Video processing workers

## 11. Infrastructure Concept

Client App
↓
NestJS API
↓
Services
Listings / Videos / Intent

↓
PostgreSQL
↓
Cloudflare R2

## 12. Security

DTO validation
JWT authentication (future)
Rate limiting
Request logging

## 13. AI Features

Video transcription
Automatic tagging
Property feature extraction
Buyer intent scoring

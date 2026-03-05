# Nodeara Backend (NestJS) -- Architecture Guide

## Overview

Nodeara backend is built using **NestJS**, a modular Node.js framework
designed for scalable systems.

Modules currently implemented: - Events - Videos - Surveys - Intent -
Listings

Server runs at: http://localhost:3000

Example endpoint: GET /listings

------------------------------------------------------------------------

## Project Structure

src/ ├ events/ ├ videos/ ├ surveys/ ├ intent/ └ listings/ ├ dto/ │ └
create-listing.dto.ts ├ listings.controller.ts ├ listings.service.ts └
listings.module.ts

------------------------------------------------------------------------

## main.ts

Responsible for bootstrapping the NestJS server.

import { ValidationPipe } from '@nestjs/common'; import { NestFactory }
from '@nestjs/core'; import { AppModule } from './app.module';

async function bootstrap() { const app = await
NestFactory.create(AppModule);

app.useGlobalPipes( new ValidationPipe({ whitelist: true, transform:
true, forbidNonWhitelisted: true, }), );

await app.listen(3000); }

bootstrap();

Purpose: - Starts NestJS server - Enables DTO validation - Removes
unsafe request fields

------------------------------------------------------------------------

## Listings API

Endpoints:

GET /listings GET /listings/:id POST /listings DELETE /listings/:id

------------------------------------------------------------------------

## Listings Controller

@Controller('listings') export class ListingsController {

constructor(private readonly listingsService: ListingsService) {}

@Get() findAll(): Listing\[\] { return this.listingsService.findAll(); }

@Get(':id') findOne(@Param('id', ParseIntPipe) id: number): Listing {
return this.listingsService.findOne(id); }

@Post() create(@Body() dto: CreateListingDto): Listing { return
this.listingsService.create(dto); }

@Delete(':id') remove(@Param('id', ParseIntPipe) id: number) { return
this.listingsService.remove(id); }

}

Purpose: - Defines API routes - Handles request parameters - Passes
logic to service layer

------------------------------------------------------------------------

## Listings Service

@Injectable() export class ListingsService {

private listings: Listing\[\] = \[\]

create(input: Omit\<Listing,'id'\|'createdAt'\>): Listing {

    const listing: Listing = {
      id: Date.now(),
      createdAt: new Date().toISOString(),
      ...input
    }

    this.listings.unshift(listing)
    return listing

}

findAll(): Listing\[\] { return this.listings }

findOne(id:number): Listing {

    const found = this.listings.find(l => l.id === id)

    if(!found){
      throw new NotFoundException(`Listing ${id} not found`)
    }

    return found

}

remove(id:number){ this.listings = this.listings.filter(l =\> l.id !==
id) return {deleted:true,id} }

}

Purpose: - Contains business logic - Stores listings - Performs CRUD
operations

------------------------------------------------------------------------

## DTO (CreateListingDto)

export class CreateListingDto {

title: string

address?: string

price?: number

coverImageUrl?: string

sourceUrl?: string

}

Purpose: - Validates incoming request body - Prevents invalid API
payloads

------------------------------------------------------------------------

## Current System Status

When running:

npm run start:dev

Console output:

Nest application successfully started

Routes loaded:

/events /videos /surveys /intent /listings

------------------------------------------------------------------------

## Recommended Next Features

1.  Listing → Video Relationship

Listing ↓ Videos

2.  Video → Intent Tracking

User watches video ↓ Intent signal generated

3.  Recommendation Engine

Intent signals ↓ Content ranking ↓ Listing recommendations

------------------------------------------------------------------------

## Suggested Production Stack

NestJS PostgreSQL Redis Prisma ORM Cloudflare R2 Docker

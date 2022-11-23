// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const BillingGroupStatus = {
    Active: "ACTIVE",
    PrimaryAccountMissing: "PRIMARY_ACCOUNT_MISSING",
} as const;

export type BillingGroupStatus = (typeof BillingGroupStatus)[keyof typeof BillingGroupStatus];

export const CustomLineItemCurrencyCode = {
    Usd: "USD",
    Cny: "CNY",
} as const;

export type CustomLineItemCurrencyCode = (typeof CustomLineItemCurrencyCode)[keyof typeof CustomLineItemCurrencyCode];

export const CustomLineItemType = {
    Fee: "FEE",
    Credit: "CREDIT",
} as const;

export type CustomLineItemType = (typeof CustomLineItemType)[keyof typeof CustomLineItemType];

export const PricingRuleBillingEntity = {
    Aws: "AWS",
    AWSMarketplace: "AWS Marketplace",
    Aispl: "AISPL",
} as const;

/**
 * The seller of services provided by AWS, their affiliates, or third-party providers selling services via AWS Marketplaces. Supported billing entities are AWS, AWS Marketplace, and AISPL.
 */
export type PricingRuleBillingEntity = (typeof PricingRuleBillingEntity)[keyof typeof PricingRuleBillingEntity];

export const PricingRuleScope = {
    Global: "GLOBAL",
    Service: "SERVICE",
    BillingEntity: "BILLING_ENTITY",
} as const;

/**
 * A term used to categorize the granularity of a Pricing Rule.
 */
export type PricingRuleScope = (typeof PricingRuleScope)[keyof typeof PricingRuleScope];

export const PricingRuleType = {
    Markup: "MARKUP",
    Discount: "DISCOUNT",
} as const;

/**
 * One of MARKUP or DISCOUNT that describes the direction of the rate that is applied to a pricing plan.
 */
export type PricingRuleType = (typeof PricingRuleType)[keyof typeof PricingRuleType];

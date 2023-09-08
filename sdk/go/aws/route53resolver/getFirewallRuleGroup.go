// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package route53resolver

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource schema for AWS::Route53Resolver::FirewallRuleGroup.
func LookupFirewallRuleGroup(ctx *pulumi.Context, args *LookupFirewallRuleGroupArgs, opts ...pulumi.InvokeOption) (*LookupFirewallRuleGroupResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupFirewallRuleGroupResult
	err := ctx.Invoke("aws-native:route53resolver:getFirewallRuleGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupFirewallRuleGroupArgs struct {
	// ResourceId
	Id string `pulumi:"id"`
}

type LookupFirewallRuleGroupResult struct {
	// Arn
	Arn *string `pulumi:"arn"`
	// Rfc3339TimeString
	CreationTime *string `pulumi:"creationTime"`
	// The id of the creator request.
	CreatorRequestId *string `pulumi:"creatorRequestId"`
	// FirewallRules
	FirewallRules []FirewallRuleGroupFirewallRule `pulumi:"firewallRules"`
	// ResourceId
	Id *string `pulumi:"id"`
	// Rfc3339TimeString
	ModificationTime *string `pulumi:"modificationTime"`
	// AccountId
	OwnerId *string `pulumi:"ownerId"`
	// Count
	RuleCount *int `pulumi:"ruleCount"`
	// ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.
	ShareStatus *FirewallRuleGroupShareStatus `pulumi:"shareStatus"`
	// ResolverFirewallRuleGroupAssociation, possible values are COMPLETE, DELETING, UPDATING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
	Status *FirewallRuleGroupStatus `pulumi:"status"`
	// FirewallRuleGroupStatus
	StatusMessage *string `pulumi:"statusMessage"`
	// Tags
	Tags []FirewallRuleGroupTag `pulumi:"tags"`
}

func LookupFirewallRuleGroupOutput(ctx *pulumi.Context, args LookupFirewallRuleGroupOutputArgs, opts ...pulumi.InvokeOption) LookupFirewallRuleGroupResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupFirewallRuleGroupResult, error) {
			args := v.(LookupFirewallRuleGroupArgs)
			r, err := LookupFirewallRuleGroup(ctx, &args, opts...)
			var s LookupFirewallRuleGroupResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupFirewallRuleGroupResultOutput)
}

type LookupFirewallRuleGroupOutputArgs struct {
	// ResourceId
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupFirewallRuleGroupOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupFirewallRuleGroupArgs)(nil)).Elem()
}

type LookupFirewallRuleGroupResultOutput struct{ *pulumi.OutputState }

func (LookupFirewallRuleGroupResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupFirewallRuleGroupResult)(nil)).Elem()
}

func (o LookupFirewallRuleGroupResultOutput) ToLookupFirewallRuleGroupResultOutput() LookupFirewallRuleGroupResultOutput {
	return o
}

func (o LookupFirewallRuleGroupResultOutput) ToLookupFirewallRuleGroupResultOutputWithContext(ctx context.Context) LookupFirewallRuleGroupResultOutput {
	return o
}

func (o LookupFirewallRuleGroupResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupFirewallRuleGroupResult] {
	return pulumix.Output[LookupFirewallRuleGroupResult]{
		OutputState: o.OutputState,
	}
}

// Arn
func (o LookupFirewallRuleGroupResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFirewallRuleGroupResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// Rfc3339TimeString
func (o LookupFirewallRuleGroupResultOutput) CreationTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFirewallRuleGroupResult) *string { return v.CreationTime }).(pulumi.StringPtrOutput)
}

// The id of the creator request.
func (o LookupFirewallRuleGroupResultOutput) CreatorRequestId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFirewallRuleGroupResult) *string { return v.CreatorRequestId }).(pulumi.StringPtrOutput)
}

// FirewallRules
func (o LookupFirewallRuleGroupResultOutput) FirewallRules() FirewallRuleGroupFirewallRuleArrayOutput {
	return o.ApplyT(func(v LookupFirewallRuleGroupResult) []FirewallRuleGroupFirewallRule { return v.FirewallRules }).(FirewallRuleGroupFirewallRuleArrayOutput)
}

// ResourceId
func (o LookupFirewallRuleGroupResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFirewallRuleGroupResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// Rfc3339TimeString
func (o LookupFirewallRuleGroupResultOutput) ModificationTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFirewallRuleGroupResult) *string { return v.ModificationTime }).(pulumi.StringPtrOutput)
}

// AccountId
func (o LookupFirewallRuleGroupResultOutput) OwnerId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFirewallRuleGroupResult) *string { return v.OwnerId }).(pulumi.StringPtrOutput)
}

// Count
func (o LookupFirewallRuleGroupResultOutput) RuleCount() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupFirewallRuleGroupResult) *int { return v.RuleCount }).(pulumi.IntPtrOutput)
}

// ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.
func (o LookupFirewallRuleGroupResultOutput) ShareStatus() FirewallRuleGroupShareStatusPtrOutput {
	return o.ApplyT(func(v LookupFirewallRuleGroupResult) *FirewallRuleGroupShareStatus { return v.ShareStatus }).(FirewallRuleGroupShareStatusPtrOutput)
}

// ResolverFirewallRuleGroupAssociation, possible values are COMPLETE, DELETING, UPDATING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
func (o LookupFirewallRuleGroupResultOutput) Status() FirewallRuleGroupStatusPtrOutput {
	return o.ApplyT(func(v LookupFirewallRuleGroupResult) *FirewallRuleGroupStatus { return v.Status }).(FirewallRuleGroupStatusPtrOutput)
}

// FirewallRuleGroupStatus
func (o LookupFirewallRuleGroupResultOutput) StatusMessage() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFirewallRuleGroupResult) *string { return v.StatusMessage }).(pulumi.StringPtrOutput)
}

// Tags
func (o LookupFirewallRuleGroupResultOutput) Tags() FirewallRuleGroupTagArrayOutput {
	return o.ApplyT(func(v LookupFirewallRuleGroupResult) []FirewallRuleGroupTag { return v.Tags }).(FirewallRuleGroupTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupFirewallRuleGroupResultOutput{})
}

// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package route53resolver

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::Route53Resolver::FirewallDomainList.
func LookupFirewallDomainList(ctx *pulumi.Context, args *LookupFirewallDomainListArgs, opts ...pulumi.InvokeOption) (*LookupFirewallDomainListResult, error) {
	var rv LookupFirewallDomainListResult
	err := ctx.Invoke("aws-native:route53resolver:getFirewallDomainList", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupFirewallDomainListArgs struct {
	// ResourceId
	Id string `pulumi:"id"`
}

type LookupFirewallDomainListResult struct {
	// Arn
	Arn *string `pulumi:"arn"`
	// Rfc3339TimeString
	CreationTime *string `pulumi:"creationTime"`
	// The id of the creator request.
	CreatorRequestId *string `pulumi:"creatorRequestId"`
	// Count
	DomainCount *int `pulumi:"domainCount"`
	// ResourceId
	Id *string `pulumi:"id"`
	// ServicePrincipal
	ManagedOwnerName *string `pulumi:"managedOwnerName"`
	// Rfc3339TimeString
	ModificationTime *string `pulumi:"modificationTime"`
	// ResolverFirewallDomainList, possible values are COMPLETE, DELETING, UPDATING, COMPLETE_IMPORT_FAILED, IMPORTING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
	Status *FirewallDomainListStatus `pulumi:"status"`
	// FirewallDomainListAssociationStatus
	StatusMessage *string `pulumi:"statusMessage"`
	// Tags
	Tags []FirewallDomainListTag `pulumi:"tags"`
}

func LookupFirewallDomainListOutput(ctx *pulumi.Context, args LookupFirewallDomainListOutputArgs, opts ...pulumi.InvokeOption) LookupFirewallDomainListResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupFirewallDomainListResult, error) {
			args := v.(LookupFirewallDomainListArgs)
			r, err := LookupFirewallDomainList(ctx, &args, opts...)
			var s LookupFirewallDomainListResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupFirewallDomainListResultOutput)
}

type LookupFirewallDomainListOutputArgs struct {
	// ResourceId
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupFirewallDomainListOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupFirewallDomainListArgs)(nil)).Elem()
}

type LookupFirewallDomainListResultOutput struct{ *pulumi.OutputState }

func (LookupFirewallDomainListResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupFirewallDomainListResult)(nil)).Elem()
}

func (o LookupFirewallDomainListResultOutput) ToLookupFirewallDomainListResultOutput() LookupFirewallDomainListResultOutput {
	return o
}

func (o LookupFirewallDomainListResultOutput) ToLookupFirewallDomainListResultOutputWithContext(ctx context.Context) LookupFirewallDomainListResultOutput {
	return o
}

// Arn
func (o LookupFirewallDomainListResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFirewallDomainListResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// Rfc3339TimeString
func (o LookupFirewallDomainListResultOutput) CreationTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFirewallDomainListResult) *string { return v.CreationTime }).(pulumi.StringPtrOutput)
}

// The id of the creator request.
func (o LookupFirewallDomainListResultOutput) CreatorRequestId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFirewallDomainListResult) *string { return v.CreatorRequestId }).(pulumi.StringPtrOutput)
}

// Count
func (o LookupFirewallDomainListResultOutput) DomainCount() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupFirewallDomainListResult) *int { return v.DomainCount }).(pulumi.IntPtrOutput)
}

// ResourceId
func (o LookupFirewallDomainListResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFirewallDomainListResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// ServicePrincipal
func (o LookupFirewallDomainListResultOutput) ManagedOwnerName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFirewallDomainListResult) *string { return v.ManagedOwnerName }).(pulumi.StringPtrOutput)
}

// Rfc3339TimeString
func (o LookupFirewallDomainListResultOutput) ModificationTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFirewallDomainListResult) *string { return v.ModificationTime }).(pulumi.StringPtrOutput)
}

// ResolverFirewallDomainList, possible values are COMPLETE, DELETING, UPDATING, COMPLETE_IMPORT_FAILED, IMPORTING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
func (o LookupFirewallDomainListResultOutput) Status() FirewallDomainListStatusPtrOutput {
	return o.ApplyT(func(v LookupFirewallDomainListResult) *FirewallDomainListStatus { return v.Status }).(FirewallDomainListStatusPtrOutput)
}

// FirewallDomainListAssociationStatus
func (o LookupFirewallDomainListResultOutput) StatusMessage() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFirewallDomainListResult) *string { return v.StatusMessage }).(pulumi.StringPtrOutput)
}

// Tags
func (o LookupFirewallDomainListResultOutput) Tags() FirewallDomainListTagArrayOutput {
	return o.ApplyT(func(v LookupFirewallDomainListResult) []FirewallDomainListTag { return v.Tags }).(FirewallDomainListTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupFirewallDomainListResultOutput{})
}

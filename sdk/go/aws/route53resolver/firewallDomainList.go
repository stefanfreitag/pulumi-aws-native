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

// Resource schema for AWS::Route53Resolver::FirewallDomainList.
type FirewallDomainList struct {
	pulumi.CustomResourceState

	// Arn
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Rfc3339TimeString
	CreationTime pulumi.StringOutput `pulumi:"creationTime"`
	// The id of the creator request.
	CreatorRequestId pulumi.StringOutput `pulumi:"creatorRequestId"`
	// Count
	DomainCount pulumi.IntOutput `pulumi:"domainCount"`
	// S3 URL to import domains from.
	DomainFileUrl pulumi.StringPtrOutput   `pulumi:"domainFileUrl"`
	Domains       pulumi.StringArrayOutput `pulumi:"domains"`
	// ServicePrincipal
	ManagedOwnerName pulumi.StringOutput `pulumi:"managedOwnerName"`
	// Rfc3339TimeString
	ModificationTime pulumi.StringOutput `pulumi:"modificationTime"`
	// FirewallDomainListName
	Name pulumi.StringPtrOutput `pulumi:"name"`
	// ResolverFirewallDomainList, possible values are COMPLETE, DELETING, UPDATING, COMPLETE_IMPORT_FAILED, IMPORTING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
	Status FirewallDomainListStatusOutput `pulumi:"status"`
	// FirewallDomainListAssociationStatus
	StatusMessage pulumi.StringOutput `pulumi:"statusMessage"`
	// Tags
	Tags FirewallDomainListTagArrayOutput `pulumi:"tags"`
}

// NewFirewallDomainList registers a new resource with the given unique name, arguments, and options.
func NewFirewallDomainList(ctx *pulumi.Context,
	name string, args *FirewallDomainListArgs, opts ...pulumi.ResourceOption) (*FirewallDomainList, error) {
	if args == nil {
		args = &FirewallDomainListArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"name",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource FirewallDomainList
	err := ctx.RegisterResource("aws-native:route53resolver:FirewallDomainList", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFirewallDomainList gets an existing FirewallDomainList resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFirewallDomainList(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FirewallDomainListState, opts ...pulumi.ResourceOption) (*FirewallDomainList, error) {
	var resource FirewallDomainList
	err := ctx.ReadResource("aws-native:route53resolver:FirewallDomainList", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering FirewallDomainList resources.
type firewallDomainListState struct {
}

type FirewallDomainListState struct {
}

func (FirewallDomainListState) ElementType() reflect.Type {
	return reflect.TypeOf((*firewallDomainListState)(nil)).Elem()
}

type firewallDomainListArgs struct {
	// S3 URL to import domains from.
	DomainFileUrl *string  `pulumi:"domainFileUrl"`
	Domains       []string `pulumi:"domains"`
	// FirewallDomainListName
	Name *string `pulumi:"name"`
	// Tags
	Tags []FirewallDomainListTag `pulumi:"tags"`
}

// The set of arguments for constructing a FirewallDomainList resource.
type FirewallDomainListArgs struct {
	// S3 URL to import domains from.
	DomainFileUrl pulumi.StringPtrInput
	Domains       pulumi.StringArrayInput
	// FirewallDomainListName
	Name pulumi.StringPtrInput
	// Tags
	Tags FirewallDomainListTagArrayInput
}

func (FirewallDomainListArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*firewallDomainListArgs)(nil)).Elem()
}

type FirewallDomainListInput interface {
	pulumi.Input

	ToFirewallDomainListOutput() FirewallDomainListOutput
	ToFirewallDomainListOutputWithContext(ctx context.Context) FirewallDomainListOutput
}

func (*FirewallDomainList) ElementType() reflect.Type {
	return reflect.TypeOf((**FirewallDomainList)(nil)).Elem()
}

func (i *FirewallDomainList) ToFirewallDomainListOutput() FirewallDomainListOutput {
	return i.ToFirewallDomainListOutputWithContext(context.Background())
}

func (i *FirewallDomainList) ToFirewallDomainListOutputWithContext(ctx context.Context) FirewallDomainListOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallDomainListOutput)
}

func (i *FirewallDomainList) ToOutput(ctx context.Context) pulumix.Output[*FirewallDomainList] {
	return pulumix.Output[*FirewallDomainList]{
		OutputState: i.ToFirewallDomainListOutputWithContext(ctx).OutputState,
	}
}

type FirewallDomainListOutput struct{ *pulumi.OutputState }

func (FirewallDomainListOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**FirewallDomainList)(nil)).Elem()
}

func (o FirewallDomainListOutput) ToFirewallDomainListOutput() FirewallDomainListOutput {
	return o
}

func (o FirewallDomainListOutput) ToFirewallDomainListOutputWithContext(ctx context.Context) FirewallDomainListOutput {
	return o
}

func (o FirewallDomainListOutput) ToOutput(ctx context.Context) pulumix.Output[*FirewallDomainList] {
	return pulumix.Output[*FirewallDomainList]{
		OutputState: o.OutputState,
	}
}

// Arn
func (o FirewallDomainListOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *FirewallDomainList) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// Rfc3339TimeString
func (o FirewallDomainListOutput) CreationTime() pulumi.StringOutput {
	return o.ApplyT(func(v *FirewallDomainList) pulumi.StringOutput { return v.CreationTime }).(pulumi.StringOutput)
}

// The id of the creator request.
func (o FirewallDomainListOutput) CreatorRequestId() pulumi.StringOutput {
	return o.ApplyT(func(v *FirewallDomainList) pulumi.StringOutput { return v.CreatorRequestId }).(pulumi.StringOutput)
}

// Count
func (o FirewallDomainListOutput) DomainCount() pulumi.IntOutput {
	return o.ApplyT(func(v *FirewallDomainList) pulumi.IntOutput { return v.DomainCount }).(pulumi.IntOutput)
}

// S3 URL to import domains from.
func (o FirewallDomainListOutput) DomainFileUrl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *FirewallDomainList) pulumi.StringPtrOutput { return v.DomainFileUrl }).(pulumi.StringPtrOutput)
}

func (o FirewallDomainListOutput) Domains() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *FirewallDomainList) pulumi.StringArrayOutput { return v.Domains }).(pulumi.StringArrayOutput)
}

// ServicePrincipal
func (o FirewallDomainListOutput) ManagedOwnerName() pulumi.StringOutput {
	return o.ApplyT(func(v *FirewallDomainList) pulumi.StringOutput { return v.ManagedOwnerName }).(pulumi.StringOutput)
}

// Rfc3339TimeString
func (o FirewallDomainListOutput) ModificationTime() pulumi.StringOutput {
	return o.ApplyT(func(v *FirewallDomainList) pulumi.StringOutput { return v.ModificationTime }).(pulumi.StringOutput)
}

// FirewallDomainListName
func (o FirewallDomainListOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *FirewallDomainList) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

// ResolverFirewallDomainList, possible values are COMPLETE, DELETING, UPDATING, COMPLETE_IMPORT_FAILED, IMPORTING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
func (o FirewallDomainListOutput) Status() FirewallDomainListStatusOutput {
	return o.ApplyT(func(v *FirewallDomainList) FirewallDomainListStatusOutput { return v.Status }).(FirewallDomainListStatusOutput)
}

// FirewallDomainListAssociationStatus
func (o FirewallDomainListOutput) StatusMessage() pulumi.StringOutput {
	return o.ApplyT(func(v *FirewallDomainList) pulumi.StringOutput { return v.StatusMessage }).(pulumi.StringOutput)
}

// Tags
func (o FirewallDomainListOutput) Tags() FirewallDomainListTagArrayOutput {
	return o.ApplyT(func(v *FirewallDomainList) FirewallDomainListTagArrayOutput { return v.Tags }).(FirewallDomainListTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*FirewallDomainListInput)(nil)).Elem(), &FirewallDomainList{})
	pulumi.RegisterOutputType(FirewallDomainListOutput{})
}

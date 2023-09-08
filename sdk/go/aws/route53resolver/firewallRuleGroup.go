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
type FirewallRuleGroup struct {
	pulumi.CustomResourceState

	// Arn
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Rfc3339TimeString
	CreationTime pulumi.StringOutput `pulumi:"creationTime"`
	// The id of the creator request.
	CreatorRequestId pulumi.StringOutput `pulumi:"creatorRequestId"`
	// FirewallRules
	FirewallRules FirewallRuleGroupFirewallRuleArrayOutput `pulumi:"firewallRules"`
	// Rfc3339TimeString
	ModificationTime pulumi.StringOutput `pulumi:"modificationTime"`
	// FirewallRuleGroupName
	Name pulumi.StringPtrOutput `pulumi:"name"`
	// AccountId
	OwnerId pulumi.StringOutput `pulumi:"ownerId"`
	// Count
	RuleCount pulumi.IntOutput `pulumi:"ruleCount"`
	// ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.
	ShareStatus FirewallRuleGroupShareStatusOutput `pulumi:"shareStatus"`
	// ResolverFirewallRuleGroupAssociation, possible values are COMPLETE, DELETING, UPDATING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
	Status FirewallRuleGroupStatusOutput `pulumi:"status"`
	// FirewallRuleGroupStatus
	StatusMessage pulumi.StringOutput `pulumi:"statusMessage"`
	// Tags
	Tags FirewallRuleGroupTagArrayOutput `pulumi:"tags"`
}

// NewFirewallRuleGroup registers a new resource with the given unique name, arguments, and options.
func NewFirewallRuleGroup(ctx *pulumi.Context,
	name string, args *FirewallRuleGroupArgs, opts ...pulumi.ResourceOption) (*FirewallRuleGroup, error) {
	if args == nil {
		args = &FirewallRuleGroupArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"name",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource FirewallRuleGroup
	err := ctx.RegisterResource("aws-native:route53resolver:FirewallRuleGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFirewallRuleGroup gets an existing FirewallRuleGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFirewallRuleGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FirewallRuleGroupState, opts ...pulumi.ResourceOption) (*FirewallRuleGroup, error) {
	var resource FirewallRuleGroup
	err := ctx.ReadResource("aws-native:route53resolver:FirewallRuleGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering FirewallRuleGroup resources.
type firewallRuleGroupState struct {
}

type FirewallRuleGroupState struct {
}

func (FirewallRuleGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*firewallRuleGroupState)(nil)).Elem()
}

type firewallRuleGroupArgs struct {
	// FirewallRules
	FirewallRules []FirewallRuleGroupFirewallRule `pulumi:"firewallRules"`
	// FirewallRuleGroupName
	Name *string `pulumi:"name"`
	// Tags
	Tags []FirewallRuleGroupTag `pulumi:"tags"`
}

// The set of arguments for constructing a FirewallRuleGroup resource.
type FirewallRuleGroupArgs struct {
	// FirewallRules
	FirewallRules FirewallRuleGroupFirewallRuleArrayInput
	// FirewallRuleGroupName
	Name pulumi.StringPtrInput
	// Tags
	Tags FirewallRuleGroupTagArrayInput
}

func (FirewallRuleGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*firewallRuleGroupArgs)(nil)).Elem()
}

type FirewallRuleGroupInput interface {
	pulumi.Input

	ToFirewallRuleGroupOutput() FirewallRuleGroupOutput
	ToFirewallRuleGroupOutputWithContext(ctx context.Context) FirewallRuleGroupOutput
}

func (*FirewallRuleGroup) ElementType() reflect.Type {
	return reflect.TypeOf((**FirewallRuleGroup)(nil)).Elem()
}

func (i *FirewallRuleGroup) ToFirewallRuleGroupOutput() FirewallRuleGroupOutput {
	return i.ToFirewallRuleGroupOutputWithContext(context.Background())
}

func (i *FirewallRuleGroup) ToFirewallRuleGroupOutputWithContext(ctx context.Context) FirewallRuleGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallRuleGroupOutput)
}

func (i *FirewallRuleGroup) ToOutput(ctx context.Context) pulumix.Output[*FirewallRuleGroup] {
	return pulumix.Output[*FirewallRuleGroup]{
		OutputState: i.ToFirewallRuleGroupOutputWithContext(ctx).OutputState,
	}
}

type FirewallRuleGroupOutput struct{ *pulumi.OutputState }

func (FirewallRuleGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**FirewallRuleGroup)(nil)).Elem()
}

func (o FirewallRuleGroupOutput) ToFirewallRuleGroupOutput() FirewallRuleGroupOutput {
	return o
}

func (o FirewallRuleGroupOutput) ToFirewallRuleGroupOutputWithContext(ctx context.Context) FirewallRuleGroupOutput {
	return o
}

func (o FirewallRuleGroupOutput) ToOutput(ctx context.Context) pulumix.Output[*FirewallRuleGroup] {
	return pulumix.Output[*FirewallRuleGroup]{
		OutputState: o.OutputState,
	}
}

// Arn
func (o FirewallRuleGroupOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *FirewallRuleGroup) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// Rfc3339TimeString
func (o FirewallRuleGroupOutput) CreationTime() pulumi.StringOutput {
	return o.ApplyT(func(v *FirewallRuleGroup) pulumi.StringOutput { return v.CreationTime }).(pulumi.StringOutput)
}

// The id of the creator request.
func (o FirewallRuleGroupOutput) CreatorRequestId() pulumi.StringOutput {
	return o.ApplyT(func(v *FirewallRuleGroup) pulumi.StringOutput { return v.CreatorRequestId }).(pulumi.StringOutput)
}

// FirewallRules
func (o FirewallRuleGroupOutput) FirewallRules() FirewallRuleGroupFirewallRuleArrayOutput {
	return o.ApplyT(func(v *FirewallRuleGroup) FirewallRuleGroupFirewallRuleArrayOutput { return v.FirewallRules }).(FirewallRuleGroupFirewallRuleArrayOutput)
}

// Rfc3339TimeString
func (o FirewallRuleGroupOutput) ModificationTime() pulumi.StringOutput {
	return o.ApplyT(func(v *FirewallRuleGroup) pulumi.StringOutput { return v.ModificationTime }).(pulumi.StringOutput)
}

// FirewallRuleGroupName
func (o FirewallRuleGroupOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *FirewallRuleGroup) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

// AccountId
func (o FirewallRuleGroupOutput) OwnerId() pulumi.StringOutput {
	return o.ApplyT(func(v *FirewallRuleGroup) pulumi.StringOutput { return v.OwnerId }).(pulumi.StringOutput)
}

// Count
func (o FirewallRuleGroupOutput) RuleCount() pulumi.IntOutput {
	return o.ApplyT(func(v *FirewallRuleGroup) pulumi.IntOutput { return v.RuleCount }).(pulumi.IntOutput)
}

// ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.
func (o FirewallRuleGroupOutput) ShareStatus() FirewallRuleGroupShareStatusOutput {
	return o.ApplyT(func(v *FirewallRuleGroup) FirewallRuleGroupShareStatusOutput { return v.ShareStatus }).(FirewallRuleGroupShareStatusOutput)
}

// ResolverFirewallRuleGroupAssociation, possible values are COMPLETE, DELETING, UPDATING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
func (o FirewallRuleGroupOutput) Status() FirewallRuleGroupStatusOutput {
	return o.ApplyT(func(v *FirewallRuleGroup) FirewallRuleGroupStatusOutput { return v.Status }).(FirewallRuleGroupStatusOutput)
}

// FirewallRuleGroupStatus
func (o FirewallRuleGroupOutput) StatusMessage() pulumi.StringOutput {
	return o.ApplyT(func(v *FirewallRuleGroup) pulumi.StringOutput { return v.StatusMessage }).(pulumi.StringOutput)
}

// Tags
func (o FirewallRuleGroupOutput) Tags() FirewallRuleGroupTagArrayOutput {
	return o.ApplyT(func(v *FirewallRuleGroup) FirewallRuleGroupTagArrayOutput { return v.Tags }).(FirewallRuleGroupTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*FirewallRuleGroupInput)(nil)).Elem(), &FirewallRuleGroup{})
	pulumi.RegisterOutputType(FirewallRuleGroupOutput{})
}

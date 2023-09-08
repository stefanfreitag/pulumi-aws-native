// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package networkfirewall

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource type definition for AWS::NetworkFirewall::Firewall
type Firewall struct {
	pulumi.CustomResourceState

	DeleteProtection               pulumi.BoolPtrOutput             `pulumi:"deleteProtection"`
	Description                    pulumi.StringPtrOutput           `pulumi:"description"`
	EndpointIds                    pulumi.StringArrayOutput         `pulumi:"endpointIds"`
	FirewallArn                    pulumi.StringOutput              `pulumi:"firewallArn"`
	FirewallId                     pulumi.StringOutput              `pulumi:"firewallId"`
	FirewallName                   pulumi.StringOutput              `pulumi:"firewallName"`
	FirewallPolicyArn              pulumi.StringOutput              `pulumi:"firewallPolicyArn"`
	FirewallPolicyChangeProtection pulumi.BoolPtrOutput             `pulumi:"firewallPolicyChangeProtection"`
	SubnetChangeProtection         pulumi.BoolPtrOutput             `pulumi:"subnetChangeProtection"`
	SubnetMappings                 FirewallSubnetMappingArrayOutput `pulumi:"subnetMappings"`
	Tags                           FirewallTagArrayOutput           `pulumi:"tags"`
	VpcId                          pulumi.StringOutput              `pulumi:"vpcId"`
}

// NewFirewall registers a new resource with the given unique name, arguments, and options.
func NewFirewall(ctx *pulumi.Context,
	name string, args *FirewallArgs, opts ...pulumi.ResourceOption) (*Firewall, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.FirewallPolicyArn == nil {
		return nil, errors.New("invalid value for required argument 'FirewallPolicyArn'")
	}
	if args.SubnetMappings == nil {
		return nil, errors.New("invalid value for required argument 'SubnetMappings'")
	}
	if args.VpcId == nil {
		return nil, errors.New("invalid value for required argument 'VpcId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"firewallName",
		"vpcId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Firewall
	err := ctx.RegisterResource("aws-native:networkfirewall:Firewall", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFirewall gets an existing Firewall resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFirewall(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FirewallState, opts ...pulumi.ResourceOption) (*Firewall, error) {
	var resource Firewall
	err := ctx.ReadResource("aws-native:networkfirewall:Firewall", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Firewall resources.
type firewallState struct {
}

type FirewallState struct {
}

func (FirewallState) ElementType() reflect.Type {
	return reflect.TypeOf((*firewallState)(nil)).Elem()
}

type firewallArgs struct {
	DeleteProtection               *bool                   `pulumi:"deleteProtection"`
	Description                    *string                 `pulumi:"description"`
	FirewallName                   *string                 `pulumi:"firewallName"`
	FirewallPolicyArn              string                  `pulumi:"firewallPolicyArn"`
	FirewallPolicyChangeProtection *bool                   `pulumi:"firewallPolicyChangeProtection"`
	SubnetChangeProtection         *bool                   `pulumi:"subnetChangeProtection"`
	SubnetMappings                 []FirewallSubnetMapping `pulumi:"subnetMappings"`
	Tags                           []FirewallTag           `pulumi:"tags"`
	VpcId                          string                  `pulumi:"vpcId"`
}

// The set of arguments for constructing a Firewall resource.
type FirewallArgs struct {
	DeleteProtection               pulumi.BoolPtrInput
	Description                    pulumi.StringPtrInput
	FirewallName                   pulumi.StringPtrInput
	FirewallPolicyArn              pulumi.StringInput
	FirewallPolicyChangeProtection pulumi.BoolPtrInput
	SubnetChangeProtection         pulumi.BoolPtrInput
	SubnetMappings                 FirewallSubnetMappingArrayInput
	Tags                           FirewallTagArrayInput
	VpcId                          pulumi.StringInput
}

func (FirewallArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*firewallArgs)(nil)).Elem()
}

type FirewallInput interface {
	pulumi.Input

	ToFirewallOutput() FirewallOutput
	ToFirewallOutputWithContext(ctx context.Context) FirewallOutput
}

func (*Firewall) ElementType() reflect.Type {
	return reflect.TypeOf((**Firewall)(nil)).Elem()
}

func (i *Firewall) ToFirewallOutput() FirewallOutput {
	return i.ToFirewallOutputWithContext(context.Background())
}

func (i *Firewall) ToFirewallOutputWithContext(ctx context.Context) FirewallOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallOutput)
}

func (i *Firewall) ToOutput(ctx context.Context) pulumix.Output[*Firewall] {
	return pulumix.Output[*Firewall]{
		OutputState: i.ToFirewallOutputWithContext(ctx).OutputState,
	}
}

type FirewallOutput struct{ *pulumi.OutputState }

func (FirewallOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Firewall)(nil)).Elem()
}

func (o FirewallOutput) ToFirewallOutput() FirewallOutput {
	return o
}

func (o FirewallOutput) ToFirewallOutputWithContext(ctx context.Context) FirewallOutput {
	return o
}

func (o FirewallOutput) ToOutput(ctx context.Context) pulumix.Output[*Firewall] {
	return pulumix.Output[*Firewall]{
		OutputState: o.OutputState,
	}
}

func (o FirewallOutput) DeleteProtection() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Firewall) pulumi.BoolPtrOutput { return v.DeleteProtection }).(pulumi.BoolPtrOutput)
}

func (o FirewallOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Firewall) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o FirewallOutput) EndpointIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Firewall) pulumi.StringArrayOutput { return v.EndpointIds }).(pulumi.StringArrayOutput)
}

func (o FirewallOutput) FirewallArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Firewall) pulumi.StringOutput { return v.FirewallArn }).(pulumi.StringOutput)
}

func (o FirewallOutput) FirewallId() pulumi.StringOutput {
	return o.ApplyT(func(v *Firewall) pulumi.StringOutput { return v.FirewallId }).(pulumi.StringOutput)
}

func (o FirewallOutput) FirewallName() pulumi.StringOutput {
	return o.ApplyT(func(v *Firewall) pulumi.StringOutput { return v.FirewallName }).(pulumi.StringOutput)
}

func (o FirewallOutput) FirewallPolicyArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Firewall) pulumi.StringOutput { return v.FirewallPolicyArn }).(pulumi.StringOutput)
}

func (o FirewallOutput) FirewallPolicyChangeProtection() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Firewall) pulumi.BoolPtrOutput { return v.FirewallPolicyChangeProtection }).(pulumi.BoolPtrOutput)
}

func (o FirewallOutput) SubnetChangeProtection() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Firewall) pulumi.BoolPtrOutput { return v.SubnetChangeProtection }).(pulumi.BoolPtrOutput)
}

func (o FirewallOutput) SubnetMappings() FirewallSubnetMappingArrayOutput {
	return o.ApplyT(func(v *Firewall) FirewallSubnetMappingArrayOutput { return v.SubnetMappings }).(FirewallSubnetMappingArrayOutput)
}

func (o FirewallOutput) Tags() FirewallTagArrayOutput {
	return o.ApplyT(func(v *Firewall) FirewallTagArrayOutput { return v.Tags }).(FirewallTagArrayOutput)
}

func (o FirewallOutput) VpcId() pulumi.StringOutput {
	return o.ApplyT(func(v *Firewall) pulumi.StringOutput { return v.VpcId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*FirewallInput)(nil)).Elem(), &Firewall{})
	pulumi.RegisterOutputType(FirewallOutput{})
}

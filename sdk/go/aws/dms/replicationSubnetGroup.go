// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dms

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::DMS::ReplicationSubnetGroup
//
// Deprecated: ReplicationSubnetGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type ReplicationSubnetGroup struct {
	pulumi.CustomResourceState

	ReplicationSubnetGroupDescription pulumi.StringOutput                  `pulumi:"replicationSubnetGroupDescription"`
	ReplicationSubnetGroupIdentifier  pulumi.StringPtrOutput               `pulumi:"replicationSubnetGroupIdentifier"`
	SubnetIds                         pulumi.StringArrayOutput             `pulumi:"subnetIds"`
	Tags                              ReplicationSubnetGroupTagArrayOutput `pulumi:"tags"`
}

// NewReplicationSubnetGroup registers a new resource with the given unique name, arguments, and options.
func NewReplicationSubnetGroup(ctx *pulumi.Context,
	name string, args *ReplicationSubnetGroupArgs, opts ...pulumi.ResourceOption) (*ReplicationSubnetGroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ReplicationSubnetGroupDescription == nil {
		return nil, errors.New("invalid value for required argument 'ReplicationSubnetGroupDescription'")
	}
	if args.SubnetIds == nil {
		return nil, errors.New("invalid value for required argument 'SubnetIds'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"replicationSubnetGroupIdentifier",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ReplicationSubnetGroup
	err := ctx.RegisterResource("aws-native:dms:ReplicationSubnetGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetReplicationSubnetGroup gets an existing ReplicationSubnetGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetReplicationSubnetGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ReplicationSubnetGroupState, opts ...pulumi.ResourceOption) (*ReplicationSubnetGroup, error) {
	var resource ReplicationSubnetGroup
	err := ctx.ReadResource("aws-native:dms:ReplicationSubnetGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ReplicationSubnetGroup resources.
type replicationSubnetGroupState struct {
}

type ReplicationSubnetGroupState struct {
}

func (ReplicationSubnetGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*replicationSubnetGroupState)(nil)).Elem()
}

type replicationSubnetGroupArgs struct {
	ReplicationSubnetGroupDescription string                      `pulumi:"replicationSubnetGroupDescription"`
	ReplicationSubnetGroupIdentifier  *string                     `pulumi:"replicationSubnetGroupIdentifier"`
	SubnetIds                         []string                    `pulumi:"subnetIds"`
	Tags                              []ReplicationSubnetGroupTag `pulumi:"tags"`
}

// The set of arguments for constructing a ReplicationSubnetGroup resource.
type ReplicationSubnetGroupArgs struct {
	ReplicationSubnetGroupDescription pulumi.StringInput
	ReplicationSubnetGroupIdentifier  pulumi.StringPtrInput
	SubnetIds                         pulumi.StringArrayInput
	Tags                              ReplicationSubnetGroupTagArrayInput
}

func (ReplicationSubnetGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*replicationSubnetGroupArgs)(nil)).Elem()
}

type ReplicationSubnetGroupInput interface {
	pulumi.Input

	ToReplicationSubnetGroupOutput() ReplicationSubnetGroupOutput
	ToReplicationSubnetGroupOutputWithContext(ctx context.Context) ReplicationSubnetGroupOutput
}

func (*ReplicationSubnetGroup) ElementType() reflect.Type {
	return reflect.TypeOf((**ReplicationSubnetGroup)(nil)).Elem()
}

func (i *ReplicationSubnetGroup) ToReplicationSubnetGroupOutput() ReplicationSubnetGroupOutput {
	return i.ToReplicationSubnetGroupOutputWithContext(context.Background())
}

func (i *ReplicationSubnetGroup) ToReplicationSubnetGroupOutputWithContext(ctx context.Context) ReplicationSubnetGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ReplicationSubnetGroupOutput)
}

func (i *ReplicationSubnetGroup) ToOutput(ctx context.Context) pulumix.Output[*ReplicationSubnetGroup] {
	return pulumix.Output[*ReplicationSubnetGroup]{
		OutputState: i.ToReplicationSubnetGroupOutputWithContext(ctx).OutputState,
	}
}

type ReplicationSubnetGroupOutput struct{ *pulumi.OutputState }

func (ReplicationSubnetGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ReplicationSubnetGroup)(nil)).Elem()
}

func (o ReplicationSubnetGroupOutput) ToReplicationSubnetGroupOutput() ReplicationSubnetGroupOutput {
	return o
}

func (o ReplicationSubnetGroupOutput) ToReplicationSubnetGroupOutputWithContext(ctx context.Context) ReplicationSubnetGroupOutput {
	return o
}

func (o ReplicationSubnetGroupOutput) ToOutput(ctx context.Context) pulumix.Output[*ReplicationSubnetGroup] {
	return pulumix.Output[*ReplicationSubnetGroup]{
		OutputState: o.OutputState,
	}
}

func (o ReplicationSubnetGroupOutput) ReplicationSubnetGroupDescription() pulumi.StringOutput {
	return o.ApplyT(func(v *ReplicationSubnetGroup) pulumi.StringOutput { return v.ReplicationSubnetGroupDescription }).(pulumi.StringOutput)
}

func (o ReplicationSubnetGroupOutput) ReplicationSubnetGroupIdentifier() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ReplicationSubnetGroup) pulumi.StringPtrOutput { return v.ReplicationSubnetGroupIdentifier }).(pulumi.StringPtrOutput)
}

func (o ReplicationSubnetGroupOutput) SubnetIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *ReplicationSubnetGroup) pulumi.StringArrayOutput { return v.SubnetIds }).(pulumi.StringArrayOutput)
}

func (o ReplicationSubnetGroupOutput) Tags() ReplicationSubnetGroupTagArrayOutput {
	return o.ApplyT(func(v *ReplicationSubnetGroup) ReplicationSubnetGroupTagArrayOutput { return v.Tags }).(ReplicationSubnetGroupTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ReplicationSubnetGroupInput)(nil)).Elem(), &ReplicationSubnetGroup{})
	pulumi.RegisterOutputType(ReplicationSubnetGroupOutput{})
}

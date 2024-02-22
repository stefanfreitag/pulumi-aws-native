// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package memorydb

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::MemoryDB::ACL
type Acl struct {
	pulumi.CustomResourceState

	// The name of the acl.
	AclName pulumi.StringOutput `pulumi:"aclName"`
	// The Amazon Resource Name (ARN) of the acl.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Indicates acl status. Can be "creating", "active", "modifying", "deleting".
	Status pulumi.StringOutput `pulumi:"status"`
	// An array of key-value pairs to apply to this cluster.
	Tags aws.TagArrayOutput `pulumi:"tags"`
	// List of users associated to this acl.
	UserNames pulumi.StringArrayOutput `pulumi:"userNames"`
}

// NewAcl registers a new resource with the given unique name, arguments, and options.
func NewAcl(ctx *pulumi.Context,
	name string, args *AclArgs, opts ...pulumi.ResourceOption) (*Acl, error) {
	if args == nil {
		args = &AclArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"aclName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Acl
	err := ctx.RegisterResource("aws-native:memorydb:Acl", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAcl gets an existing Acl resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAcl(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AclState, opts ...pulumi.ResourceOption) (*Acl, error) {
	var resource Acl
	err := ctx.ReadResource("aws-native:memorydb:Acl", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Acl resources.
type aclState struct {
}

type AclState struct {
}

func (AclState) ElementType() reflect.Type {
	return reflect.TypeOf((*aclState)(nil)).Elem()
}

type aclArgs struct {
	// The name of the acl.
	AclName *string `pulumi:"aclName"`
	// An array of key-value pairs to apply to this cluster.
	Tags []aws.Tag `pulumi:"tags"`
	// List of users associated to this acl.
	UserNames []string `pulumi:"userNames"`
}

// The set of arguments for constructing a Acl resource.
type AclArgs struct {
	// The name of the acl.
	AclName pulumi.StringPtrInput
	// An array of key-value pairs to apply to this cluster.
	Tags aws.TagArrayInput
	// List of users associated to this acl.
	UserNames pulumi.StringArrayInput
}

func (AclArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*aclArgs)(nil)).Elem()
}

type AclInput interface {
	pulumi.Input

	ToAclOutput() AclOutput
	ToAclOutputWithContext(ctx context.Context) AclOutput
}

func (*Acl) ElementType() reflect.Type {
	return reflect.TypeOf((**Acl)(nil)).Elem()
}

func (i *Acl) ToAclOutput() AclOutput {
	return i.ToAclOutputWithContext(context.Background())
}

func (i *Acl) ToAclOutputWithContext(ctx context.Context) AclOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AclOutput)
}

type AclOutput struct{ *pulumi.OutputState }

func (AclOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Acl)(nil)).Elem()
}

func (o AclOutput) ToAclOutput() AclOutput {
	return o
}

func (o AclOutput) ToAclOutputWithContext(ctx context.Context) AclOutput {
	return o
}

// The name of the acl.
func (o AclOutput) AclName() pulumi.StringOutput {
	return o.ApplyT(func(v *Acl) pulumi.StringOutput { return v.AclName }).(pulumi.StringOutput)
}

// The Amazon Resource Name (ARN) of the acl.
func (o AclOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Acl) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// Indicates acl status. Can be "creating", "active", "modifying", "deleting".
func (o AclOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v *Acl) pulumi.StringOutput { return v.Status }).(pulumi.StringOutput)
}

// An array of key-value pairs to apply to this cluster.
func (o AclOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *Acl) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

// List of users associated to this acl.
func (o AclOutput) UserNames() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Acl) pulumi.StringArrayOutput { return v.UserNames }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AclInput)(nil)).Elem(), &Acl{})
	pulumi.RegisterOutputType(AclOutput{})
}

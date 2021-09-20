// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cassandra

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::Cassandra::Keyspace
type Keyspace struct {
	pulumi.CustomResourceState

	// Name for Cassandra keyspace
	KeyspaceName pulumi.StringPtrOutput `pulumi:"keyspaceName"`
	Tags         KeyspaceTagArrayOutput `pulumi:"tags"`
}

// NewKeyspace registers a new resource with the given unique name, arguments, and options.
func NewKeyspace(ctx *pulumi.Context,
	name string, args *KeyspaceArgs, opts ...pulumi.ResourceOption) (*Keyspace, error) {
	if args == nil {
		args = &KeyspaceArgs{}
	}

	var resource Keyspace
	err := ctx.RegisterResource("aws-native:cassandra:Keyspace", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetKeyspace gets an existing Keyspace resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetKeyspace(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *KeyspaceState, opts ...pulumi.ResourceOption) (*Keyspace, error) {
	var resource Keyspace
	err := ctx.ReadResource("aws-native:cassandra:Keyspace", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Keyspace resources.
type keyspaceState struct {
}

type KeyspaceState struct {
}

func (KeyspaceState) ElementType() reflect.Type {
	return reflect.TypeOf((*keyspaceState)(nil)).Elem()
}

type keyspaceArgs struct {
	// Name for Cassandra keyspace
	KeyspaceName *string       `pulumi:"keyspaceName"`
	Tags         []KeyspaceTag `pulumi:"tags"`
}

// The set of arguments for constructing a Keyspace resource.
type KeyspaceArgs struct {
	// Name for Cassandra keyspace
	KeyspaceName pulumi.StringPtrInput
	Tags         KeyspaceTagArrayInput
}

func (KeyspaceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*keyspaceArgs)(nil)).Elem()
}

type KeyspaceInput interface {
	pulumi.Input

	ToKeyspaceOutput() KeyspaceOutput
	ToKeyspaceOutputWithContext(ctx context.Context) KeyspaceOutput
}

func (*Keyspace) ElementType() reflect.Type {
	return reflect.TypeOf((*Keyspace)(nil))
}

func (i *Keyspace) ToKeyspaceOutput() KeyspaceOutput {
	return i.ToKeyspaceOutputWithContext(context.Background())
}

func (i *Keyspace) ToKeyspaceOutputWithContext(ctx context.Context) KeyspaceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KeyspaceOutput)
}

type KeyspaceOutput struct{ *pulumi.OutputState }

func (KeyspaceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Keyspace)(nil))
}

func (o KeyspaceOutput) ToKeyspaceOutput() KeyspaceOutput {
	return o
}

func (o KeyspaceOutput) ToKeyspaceOutputWithContext(ctx context.Context) KeyspaceOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(KeyspaceOutput{})
}

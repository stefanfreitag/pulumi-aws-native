// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package servicediscovery

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::ServiceDiscovery::HttpNamespace
//
// Deprecated: HttpNamespace is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type HttpNamespace struct {
	pulumi.CustomResourceState

	Arn         pulumi.StringOutput         `pulumi:"arn"`
	Description pulumi.StringPtrOutput      `pulumi:"description"`
	Name        pulumi.StringOutput         `pulumi:"name"`
	Tags        HttpNamespaceTagArrayOutput `pulumi:"tags"`
}

// NewHttpNamespace registers a new resource with the given unique name, arguments, and options.
func NewHttpNamespace(ctx *pulumi.Context,
	name string, args *HttpNamespaceArgs, opts ...pulumi.ResourceOption) (*HttpNamespace, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	var resource HttpNamespace
	err := ctx.RegisterResource("aws-native:servicediscovery:HttpNamespace", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetHttpNamespace gets an existing HttpNamespace resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHttpNamespace(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *HttpNamespaceState, opts ...pulumi.ResourceOption) (*HttpNamespace, error) {
	var resource HttpNamespace
	err := ctx.ReadResource("aws-native:servicediscovery:HttpNamespace", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering HttpNamespace resources.
type httpNamespaceState struct {
}

type HttpNamespaceState struct {
}

func (HttpNamespaceState) ElementType() reflect.Type {
	return reflect.TypeOf((*httpNamespaceState)(nil)).Elem()
}

type httpNamespaceArgs struct {
	Description *string            `pulumi:"description"`
	Name        string             `pulumi:"name"`
	Tags        []HttpNamespaceTag `pulumi:"tags"`
}

// The set of arguments for constructing a HttpNamespace resource.
type HttpNamespaceArgs struct {
	Description pulumi.StringPtrInput
	Name        pulumi.StringInput
	Tags        HttpNamespaceTagArrayInput
}

func (HttpNamespaceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*httpNamespaceArgs)(nil)).Elem()
}

type HttpNamespaceInput interface {
	pulumi.Input

	ToHttpNamespaceOutput() HttpNamespaceOutput
	ToHttpNamespaceOutputWithContext(ctx context.Context) HttpNamespaceOutput
}

func (*HttpNamespace) ElementType() reflect.Type {
	return reflect.TypeOf((*HttpNamespace)(nil))
}

func (i *HttpNamespace) ToHttpNamespaceOutput() HttpNamespaceOutput {
	return i.ToHttpNamespaceOutputWithContext(context.Background())
}

func (i *HttpNamespace) ToHttpNamespaceOutputWithContext(ctx context.Context) HttpNamespaceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HttpNamespaceOutput)
}

type HttpNamespaceOutput struct{ *pulumi.OutputState }

func (HttpNamespaceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*HttpNamespace)(nil))
}

func (o HttpNamespaceOutput) ToHttpNamespaceOutput() HttpNamespaceOutput {
	return o
}

func (o HttpNamespaceOutput) ToHttpNamespaceOutputWithContext(ctx context.Context) HttpNamespaceOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(HttpNamespaceOutput{})
}

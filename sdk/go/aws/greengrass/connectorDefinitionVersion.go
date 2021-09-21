// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package greengrass

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Greengrass::ConnectorDefinitionVersion
//
// Deprecated: ConnectorDefinitionVersion is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type ConnectorDefinitionVersion struct {
	pulumi.CustomResourceState

	ConnectorDefinitionId pulumi.StringOutput                            `pulumi:"connectorDefinitionId"`
	Connectors            ConnectorDefinitionVersionConnectorArrayOutput `pulumi:"connectors"`
}

// NewConnectorDefinitionVersion registers a new resource with the given unique name, arguments, and options.
func NewConnectorDefinitionVersion(ctx *pulumi.Context,
	name string, args *ConnectorDefinitionVersionArgs, opts ...pulumi.ResourceOption) (*ConnectorDefinitionVersion, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ConnectorDefinitionId == nil {
		return nil, errors.New("invalid value for required argument 'ConnectorDefinitionId'")
	}
	if args.Connectors == nil {
		return nil, errors.New("invalid value for required argument 'Connectors'")
	}
	var resource ConnectorDefinitionVersion
	err := ctx.RegisterResource("aws-native:greengrass:ConnectorDefinitionVersion", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetConnectorDefinitionVersion gets an existing ConnectorDefinitionVersion resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConnectorDefinitionVersion(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ConnectorDefinitionVersionState, opts ...pulumi.ResourceOption) (*ConnectorDefinitionVersion, error) {
	var resource ConnectorDefinitionVersion
	err := ctx.ReadResource("aws-native:greengrass:ConnectorDefinitionVersion", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ConnectorDefinitionVersion resources.
type connectorDefinitionVersionState struct {
}

type ConnectorDefinitionVersionState struct {
}

func (ConnectorDefinitionVersionState) ElementType() reflect.Type {
	return reflect.TypeOf((*connectorDefinitionVersionState)(nil)).Elem()
}

type connectorDefinitionVersionArgs struct {
	ConnectorDefinitionId string                                `pulumi:"connectorDefinitionId"`
	Connectors            []ConnectorDefinitionVersionConnector `pulumi:"connectors"`
}

// The set of arguments for constructing a ConnectorDefinitionVersion resource.
type ConnectorDefinitionVersionArgs struct {
	ConnectorDefinitionId pulumi.StringInput
	Connectors            ConnectorDefinitionVersionConnectorArrayInput
}

func (ConnectorDefinitionVersionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*connectorDefinitionVersionArgs)(nil)).Elem()
}

type ConnectorDefinitionVersionInput interface {
	pulumi.Input

	ToConnectorDefinitionVersionOutput() ConnectorDefinitionVersionOutput
	ToConnectorDefinitionVersionOutputWithContext(ctx context.Context) ConnectorDefinitionVersionOutput
}

func (*ConnectorDefinitionVersion) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectorDefinitionVersion)(nil))
}

func (i *ConnectorDefinitionVersion) ToConnectorDefinitionVersionOutput() ConnectorDefinitionVersionOutput {
	return i.ToConnectorDefinitionVersionOutputWithContext(context.Background())
}

func (i *ConnectorDefinitionVersion) ToConnectorDefinitionVersionOutputWithContext(ctx context.Context) ConnectorDefinitionVersionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectorDefinitionVersionOutput)
}

type ConnectorDefinitionVersionOutput struct{ *pulumi.OutputState }

func (ConnectorDefinitionVersionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectorDefinitionVersion)(nil))
}

func (o ConnectorDefinitionVersionOutput) ToConnectorDefinitionVersionOutput() ConnectorDefinitionVersionOutput {
	return o
}

func (o ConnectorDefinitionVersionOutput) ToConnectorDefinitionVersionOutputWithContext(ctx context.Context) ConnectorDefinitionVersionOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ConnectorDefinitionVersionOutput{})
}

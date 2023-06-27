// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package appflow

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::AppFlow::Connector
type Connector struct {
	pulumi.CustomResourceState

	//  The arn of the connector. The arn is unique for each ConnectorRegistration in your AWS account.
	ConnectorArn pulumi.StringOutput `pulumi:"connectorArn"`
	//  The name of the connector. The name is unique for each ConnectorRegistration in your AWS account.
	ConnectorLabel pulumi.StringPtrOutput `pulumi:"connectorLabel"`
	// Contains information about the configuration of the connector being registered.
	ConnectorProvisioningConfig ConnectorProvisioningConfigOutput `pulumi:"connectorProvisioningConfig"`
	// The provisioning type of the connector. Currently the only supported value is LAMBDA.
	ConnectorProvisioningType pulumi.StringOutput `pulumi:"connectorProvisioningType"`
	// A description about the connector that's being registered.
	Description pulumi.StringPtrOutput `pulumi:"description"`
}

// NewConnector registers a new resource with the given unique name, arguments, and options.
func NewConnector(ctx *pulumi.Context,
	name string, args *ConnectorArgs, opts ...pulumi.ResourceOption) (*Connector, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ConnectorProvisioningConfig == nil {
		return nil, errors.New("invalid value for required argument 'ConnectorProvisioningConfig'")
	}
	if args.ConnectorProvisioningType == nil {
		return nil, errors.New("invalid value for required argument 'ConnectorProvisioningType'")
	}
	var resource Connector
	err := ctx.RegisterResource("aws-native:appflow:Connector", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetConnector gets an existing Connector resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConnector(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ConnectorState, opts ...pulumi.ResourceOption) (*Connector, error) {
	var resource Connector
	err := ctx.ReadResource("aws-native:appflow:Connector", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Connector resources.
type connectorState struct {
}

type ConnectorState struct {
}

func (ConnectorState) ElementType() reflect.Type {
	return reflect.TypeOf((*connectorState)(nil)).Elem()
}

type connectorArgs struct {
	//  The name of the connector. The name is unique for each ConnectorRegistration in your AWS account.
	ConnectorLabel *string `pulumi:"connectorLabel"`
	// Contains information about the configuration of the connector being registered.
	ConnectorProvisioningConfig ConnectorProvisioningConfig `pulumi:"connectorProvisioningConfig"`
	// The provisioning type of the connector. Currently the only supported value is LAMBDA.
	ConnectorProvisioningType string `pulumi:"connectorProvisioningType"`
	// A description about the connector that's being registered.
	Description *string `pulumi:"description"`
}

// The set of arguments for constructing a Connector resource.
type ConnectorArgs struct {
	//  The name of the connector. The name is unique for each ConnectorRegistration in your AWS account.
	ConnectorLabel pulumi.StringPtrInput
	// Contains information about the configuration of the connector being registered.
	ConnectorProvisioningConfig ConnectorProvisioningConfigInput
	// The provisioning type of the connector. Currently the only supported value is LAMBDA.
	ConnectorProvisioningType pulumi.StringInput
	// A description about the connector that's being registered.
	Description pulumi.StringPtrInput
}

func (ConnectorArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*connectorArgs)(nil)).Elem()
}

type ConnectorInput interface {
	pulumi.Input

	ToConnectorOutput() ConnectorOutput
	ToConnectorOutputWithContext(ctx context.Context) ConnectorOutput
}

func (*Connector) ElementType() reflect.Type {
	return reflect.TypeOf((**Connector)(nil)).Elem()
}

func (i *Connector) ToConnectorOutput() ConnectorOutput {
	return i.ToConnectorOutputWithContext(context.Background())
}

func (i *Connector) ToConnectorOutputWithContext(ctx context.Context) ConnectorOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectorOutput)
}

type ConnectorOutput struct{ *pulumi.OutputState }

func (ConnectorOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Connector)(nil)).Elem()
}

func (o ConnectorOutput) ToConnectorOutput() ConnectorOutput {
	return o
}

func (o ConnectorOutput) ToConnectorOutputWithContext(ctx context.Context) ConnectorOutput {
	return o
}

// The arn of the connector. The arn is unique for each ConnectorRegistration in your AWS account.
func (o ConnectorOutput) ConnectorArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Connector) pulumi.StringOutput { return v.ConnectorArn }).(pulumi.StringOutput)
}

// The name of the connector. The name is unique for each ConnectorRegistration in your AWS account.
func (o ConnectorOutput) ConnectorLabel() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Connector) pulumi.StringPtrOutput { return v.ConnectorLabel }).(pulumi.StringPtrOutput)
}

// Contains information about the configuration of the connector being registered.
func (o ConnectorOutput) ConnectorProvisioningConfig() ConnectorProvisioningConfigOutput {
	return o.ApplyT(func(v *Connector) ConnectorProvisioningConfigOutput { return v.ConnectorProvisioningConfig }).(ConnectorProvisioningConfigOutput)
}

// The provisioning type of the connector. Currently the only supported value is LAMBDA.
func (o ConnectorOutput) ConnectorProvisioningType() pulumi.StringOutput {
	return o.ApplyT(func(v *Connector) pulumi.StringOutput { return v.ConnectorProvisioningType }).(pulumi.StringOutput)
}

// A description about the connector that's being registered.
func (o ConnectorOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Connector) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ConnectorInput)(nil)).Elem(), &Connector{})
	pulumi.RegisterOutputType(ConnectorOutput{})
}

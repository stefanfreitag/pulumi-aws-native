// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package kafkaconnect

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The type of client authentication used to connect to the Kafka cluster. Value NONE means that no client authentication is used.
type ConnectorKafkaClusterClientAuthenticationType string

const (
	ConnectorKafkaClusterClientAuthenticationTypeNone = ConnectorKafkaClusterClientAuthenticationType("NONE")
	ConnectorKafkaClusterClientAuthenticationTypeIam  = ConnectorKafkaClusterClientAuthenticationType("IAM")
)

func (ConnectorKafkaClusterClientAuthenticationType) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectorKafkaClusterClientAuthenticationType)(nil)).Elem()
}

func (e ConnectorKafkaClusterClientAuthenticationType) ToConnectorKafkaClusterClientAuthenticationTypeOutput() ConnectorKafkaClusterClientAuthenticationTypeOutput {
	return pulumi.ToOutput(e).(ConnectorKafkaClusterClientAuthenticationTypeOutput)
}

func (e ConnectorKafkaClusterClientAuthenticationType) ToConnectorKafkaClusterClientAuthenticationTypeOutputWithContext(ctx context.Context) ConnectorKafkaClusterClientAuthenticationTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(ConnectorKafkaClusterClientAuthenticationTypeOutput)
}

func (e ConnectorKafkaClusterClientAuthenticationType) ToConnectorKafkaClusterClientAuthenticationTypePtrOutput() ConnectorKafkaClusterClientAuthenticationTypePtrOutput {
	return e.ToConnectorKafkaClusterClientAuthenticationTypePtrOutputWithContext(context.Background())
}

func (e ConnectorKafkaClusterClientAuthenticationType) ToConnectorKafkaClusterClientAuthenticationTypePtrOutputWithContext(ctx context.Context) ConnectorKafkaClusterClientAuthenticationTypePtrOutput {
	return ConnectorKafkaClusterClientAuthenticationType(e).ToConnectorKafkaClusterClientAuthenticationTypeOutputWithContext(ctx).ToConnectorKafkaClusterClientAuthenticationTypePtrOutputWithContext(ctx)
}

func (e ConnectorKafkaClusterClientAuthenticationType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e ConnectorKafkaClusterClientAuthenticationType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e ConnectorKafkaClusterClientAuthenticationType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e ConnectorKafkaClusterClientAuthenticationType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type ConnectorKafkaClusterClientAuthenticationTypeOutput struct{ *pulumi.OutputState }

func (ConnectorKafkaClusterClientAuthenticationTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectorKafkaClusterClientAuthenticationType)(nil)).Elem()
}

func (o ConnectorKafkaClusterClientAuthenticationTypeOutput) ToConnectorKafkaClusterClientAuthenticationTypeOutput() ConnectorKafkaClusterClientAuthenticationTypeOutput {
	return o
}

func (o ConnectorKafkaClusterClientAuthenticationTypeOutput) ToConnectorKafkaClusterClientAuthenticationTypeOutputWithContext(ctx context.Context) ConnectorKafkaClusterClientAuthenticationTypeOutput {
	return o
}

func (o ConnectorKafkaClusterClientAuthenticationTypeOutput) ToConnectorKafkaClusterClientAuthenticationTypePtrOutput() ConnectorKafkaClusterClientAuthenticationTypePtrOutput {
	return o.ToConnectorKafkaClusterClientAuthenticationTypePtrOutputWithContext(context.Background())
}

func (o ConnectorKafkaClusterClientAuthenticationTypeOutput) ToConnectorKafkaClusterClientAuthenticationTypePtrOutputWithContext(ctx context.Context) ConnectorKafkaClusterClientAuthenticationTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ConnectorKafkaClusterClientAuthenticationType) *ConnectorKafkaClusterClientAuthenticationType {
		return &v
	}).(ConnectorKafkaClusterClientAuthenticationTypePtrOutput)
}

func (o ConnectorKafkaClusterClientAuthenticationTypeOutput) ToOutput(ctx context.Context) pulumix.Output[ConnectorKafkaClusterClientAuthenticationType] {
	return pulumix.Output[ConnectorKafkaClusterClientAuthenticationType]{
		OutputState: o.OutputState,
	}
}

func (o ConnectorKafkaClusterClientAuthenticationTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o ConnectorKafkaClusterClientAuthenticationTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ConnectorKafkaClusterClientAuthenticationType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o ConnectorKafkaClusterClientAuthenticationTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ConnectorKafkaClusterClientAuthenticationTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ConnectorKafkaClusterClientAuthenticationType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type ConnectorKafkaClusterClientAuthenticationTypePtrOutput struct{ *pulumi.OutputState }

func (ConnectorKafkaClusterClientAuthenticationTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ConnectorKafkaClusterClientAuthenticationType)(nil)).Elem()
}

func (o ConnectorKafkaClusterClientAuthenticationTypePtrOutput) ToConnectorKafkaClusterClientAuthenticationTypePtrOutput() ConnectorKafkaClusterClientAuthenticationTypePtrOutput {
	return o
}

func (o ConnectorKafkaClusterClientAuthenticationTypePtrOutput) ToConnectorKafkaClusterClientAuthenticationTypePtrOutputWithContext(ctx context.Context) ConnectorKafkaClusterClientAuthenticationTypePtrOutput {
	return o
}

func (o ConnectorKafkaClusterClientAuthenticationTypePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*ConnectorKafkaClusterClientAuthenticationType] {
	return pulumix.Output[*ConnectorKafkaClusterClientAuthenticationType]{
		OutputState: o.OutputState,
	}
}

func (o ConnectorKafkaClusterClientAuthenticationTypePtrOutput) Elem() ConnectorKafkaClusterClientAuthenticationTypeOutput {
	return o.ApplyT(func(v *ConnectorKafkaClusterClientAuthenticationType) ConnectorKafkaClusterClientAuthenticationType {
		if v != nil {
			return *v
		}
		var ret ConnectorKafkaClusterClientAuthenticationType
		return ret
	}).(ConnectorKafkaClusterClientAuthenticationTypeOutput)
}

func (o ConnectorKafkaClusterClientAuthenticationTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ConnectorKafkaClusterClientAuthenticationTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *ConnectorKafkaClusterClientAuthenticationType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// ConnectorKafkaClusterClientAuthenticationTypeInput is an input type that accepts ConnectorKafkaClusterClientAuthenticationTypeArgs and ConnectorKafkaClusterClientAuthenticationTypeOutput values.
// You can construct a concrete instance of `ConnectorKafkaClusterClientAuthenticationTypeInput` via:
//
//	ConnectorKafkaClusterClientAuthenticationTypeArgs{...}
type ConnectorKafkaClusterClientAuthenticationTypeInput interface {
	pulumi.Input

	ToConnectorKafkaClusterClientAuthenticationTypeOutput() ConnectorKafkaClusterClientAuthenticationTypeOutput
	ToConnectorKafkaClusterClientAuthenticationTypeOutputWithContext(context.Context) ConnectorKafkaClusterClientAuthenticationTypeOutput
}

var connectorKafkaClusterClientAuthenticationTypePtrType = reflect.TypeOf((**ConnectorKafkaClusterClientAuthenticationType)(nil)).Elem()

type ConnectorKafkaClusterClientAuthenticationTypePtrInput interface {
	pulumi.Input

	ToConnectorKafkaClusterClientAuthenticationTypePtrOutput() ConnectorKafkaClusterClientAuthenticationTypePtrOutput
	ToConnectorKafkaClusterClientAuthenticationTypePtrOutputWithContext(context.Context) ConnectorKafkaClusterClientAuthenticationTypePtrOutput
}

type connectorKafkaClusterClientAuthenticationTypePtr string

func ConnectorKafkaClusterClientAuthenticationTypePtr(v string) ConnectorKafkaClusterClientAuthenticationTypePtrInput {
	return (*connectorKafkaClusterClientAuthenticationTypePtr)(&v)
}

func (*connectorKafkaClusterClientAuthenticationTypePtr) ElementType() reflect.Type {
	return connectorKafkaClusterClientAuthenticationTypePtrType
}

func (in *connectorKafkaClusterClientAuthenticationTypePtr) ToConnectorKafkaClusterClientAuthenticationTypePtrOutput() ConnectorKafkaClusterClientAuthenticationTypePtrOutput {
	return pulumi.ToOutput(in).(ConnectorKafkaClusterClientAuthenticationTypePtrOutput)
}

func (in *connectorKafkaClusterClientAuthenticationTypePtr) ToConnectorKafkaClusterClientAuthenticationTypePtrOutputWithContext(ctx context.Context) ConnectorKafkaClusterClientAuthenticationTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(ConnectorKafkaClusterClientAuthenticationTypePtrOutput)
}

func (in *connectorKafkaClusterClientAuthenticationTypePtr) ToOutput(ctx context.Context) pulumix.Output[*ConnectorKafkaClusterClientAuthenticationType] {
	return pulumix.Output[*ConnectorKafkaClusterClientAuthenticationType]{
		OutputState: in.ToConnectorKafkaClusterClientAuthenticationTypePtrOutputWithContext(ctx).OutputState,
	}
}

// The type of encryption in transit to the Kafka cluster.
type ConnectorKafkaClusterEncryptionInTransitType string

const (
	ConnectorKafkaClusterEncryptionInTransitTypePlaintext = ConnectorKafkaClusterEncryptionInTransitType("PLAINTEXT")
	ConnectorKafkaClusterEncryptionInTransitTypeTls       = ConnectorKafkaClusterEncryptionInTransitType("TLS")
)

func (ConnectorKafkaClusterEncryptionInTransitType) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectorKafkaClusterEncryptionInTransitType)(nil)).Elem()
}

func (e ConnectorKafkaClusterEncryptionInTransitType) ToConnectorKafkaClusterEncryptionInTransitTypeOutput() ConnectorKafkaClusterEncryptionInTransitTypeOutput {
	return pulumi.ToOutput(e).(ConnectorKafkaClusterEncryptionInTransitTypeOutput)
}

func (e ConnectorKafkaClusterEncryptionInTransitType) ToConnectorKafkaClusterEncryptionInTransitTypeOutputWithContext(ctx context.Context) ConnectorKafkaClusterEncryptionInTransitTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(ConnectorKafkaClusterEncryptionInTransitTypeOutput)
}

func (e ConnectorKafkaClusterEncryptionInTransitType) ToConnectorKafkaClusterEncryptionInTransitTypePtrOutput() ConnectorKafkaClusterEncryptionInTransitTypePtrOutput {
	return e.ToConnectorKafkaClusterEncryptionInTransitTypePtrOutputWithContext(context.Background())
}

func (e ConnectorKafkaClusterEncryptionInTransitType) ToConnectorKafkaClusterEncryptionInTransitTypePtrOutputWithContext(ctx context.Context) ConnectorKafkaClusterEncryptionInTransitTypePtrOutput {
	return ConnectorKafkaClusterEncryptionInTransitType(e).ToConnectorKafkaClusterEncryptionInTransitTypeOutputWithContext(ctx).ToConnectorKafkaClusterEncryptionInTransitTypePtrOutputWithContext(ctx)
}

func (e ConnectorKafkaClusterEncryptionInTransitType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e ConnectorKafkaClusterEncryptionInTransitType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e ConnectorKafkaClusterEncryptionInTransitType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e ConnectorKafkaClusterEncryptionInTransitType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type ConnectorKafkaClusterEncryptionInTransitTypeOutput struct{ *pulumi.OutputState }

func (ConnectorKafkaClusterEncryptionInTransitTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectorKafkaClusterEncryptionInTransitType)(nil)).Elem()
}

func (o ConnectorKafkaClusterEncryptionInTransitTypeOutput) ToConnectorKafkaClusterEncryptionInTransitTypeOutput() ConnectorKafkaClusterEncryptionInTransitTypeOutput {
	return o
}

func (o ConnectorKafkaClusterEncryptionInTransitTypeOutput) ToConnectorKafkaClusterEncryptionInTransitTypeOutputWithContext(ctx context.Context) ConnectorKafkaClusterEncryptionInTransitTypeOutput {
	return o
}

func (o ConnectorKafkaClusterEncryptionInTransitTypeOutput) ToConnectorKafkaClusterEncryptionInTransitTypePtrOutput() ConnectorKafkaClusterEncryptionInTransitTypePtrOutput {
	return o.ToConnectorKafkaClusterEncryptionInTransitTypePtrOutputWithContext(context.Background())
}

func (o ConnectorKafkaClusterEncryptionInTransitTypeOutput) ToConnectorKafkaClusterEncryptionInTransitTypePtrOutputWithContext(ctx context.Context) ConnectorKafkaClusterEncryptionInTransitTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ConnectorKafkaClusterEncryptionInTransitType) *ConnectorKafkaClusterEncryptionInTransitType {
		return &v
	}).(ConnectorKafkaClusterEncryptionInTransitTypePtrOutput)
}

func (o ConnectorKafkaClusterEncryptionInTransitTypeOutput) ToOutput(ctx context.Context) pulumix.Output[ConnectorKafkaClusterEncryptionInTransitType] {
	return pulumix.Output[ConnectorKafkaClusterEncryptionInTransitType]{
		OutputState: o.OutputState,
	}
}

func (o ConnectorKafkaClusterEncryptionInTransitTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o ConnectorKafkaClusterEncryptionInTransitTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ConnectorKafkaClusterEncryptionInTransitType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o ConnectorKafkaClusterEncryptionInTransitTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ConnectorKafkaClusterEncryptionInTransitTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ConnectorKafkaClusterEncryptionInTransitType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type ConnectorKafkaClusterEncryptionInTransitTypePtrOutput struct{ *pulumi.OutputState }

func (ConnectorKafkaClusterEncryptionInTransitTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ConnectorKafkaClusterEncryptionInTransitType)(nil)).Elem()
}

func (o ConnectorKafkaClusterEncryptionInTransitTypePtrOutput) ToConnectorKafkaClusterEncryptionInTransitTypePtrOutput() ConnectorKafkaClusterEncryptionInTransitTypePtrOutput {
	return o
}

func (o ConnectorKafkaClusterEncryptionInTransitTypePtrOutput) ToConnectorKafkaClusterEncryptionInTransitTypePtrOutputWithContext(ctx context.Context) ConnectorKafkaClusterEncryptionInTransitTypePtrOutput {
	return o
}

func (o ConnectorKafkaClusterEncryptionInTransitTypePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*ConnectorKafkaClusterEncryptionInTransitType] {
	return pulumix.Output[*ConnectorKafkaClusterEncryptionInTransitType]{
		OutputState: o.OutputState,
	}
}

func (o ConnectorKafkaClusterEncryptionInTransitTypePtrOutput) Elem() ConnectorKafkaClusterEncryptionInTransitTypeOutput {
	return o.ApplyT(func(v *ConnectorKafkaClusterEncryptionInTransitType) ConnectorKafkaClusterEncryptionInTransitType {
		if v != nil {
			return *v
		}
		var ret ConnectorKafkaClusterEncryptionInTransitType
		return ret
	}).(ConnectorKafkaClusterEncryptionInTransitTypeOutput)
}

func (o ConnectorKafkaClusterEncryptionInTransitTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ConnectorKafkaClusterEncryptionInTransitTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *ConnectorKafkaClusterEncryptionInTransitType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// ConnectorKafkaClusterEncryptionInTransitTypeInput is an input type that accepts ConnectorKafkaClusterEncryptionInTransitTypeArgs and ConnectorKafkaClusterEncryptionInTransitTypeOutput values.
// You can construct a concrete instance of `ConnectorKafkaClusterEncryptionInTransitTypeInput` via:
//
//	ConnectorKafkaClusterEncryptionInTransitTypeArgs{...}
type ConnectorKafkaClusterEncryptionInTransitTypeInput interface {
	pulumi.Input

	ToConnectorKafkaClusterEncryptionInTransitTypeOutput() ConnectorKafkaClusterEncryptionInTransitTypeOutput
	ToConnectorKafkaClusterEncryptionInTransitTypeOutputWithContext(context.Context) ConnectorKafkaClusterEncryptionInTransitTypeOutput
}

var connectorKafkaClusterEncryptionInTransitTypePtrType = reflect.TypeOf((**ConnectorKafkaClusterEncryptionInTransitType)(nil)).Elem()

type ConnectorKafkaClusterEncryptionInTransitTypePtrInput interface {
	pulumi.Input

	ToConnectorKafkaClusterEncryptionInTransitTypePtrOutput() ConnectorKafkaClusterEncryptionInTransitTypePtrOutput
	ToConnectorKafkaClusterEncryptionInTransitTypePtrOutputWithContext(context.Context) ConnectorKafkaClusterEncryptionInTransitTypePtrOutput
}

type connectorKafkaClusterEncryptionInTransitTypePtr string

func ConnectorKafkaClusterEncryptionInTransitTypePtr(v string) ConnectorKafkaClusterEncryptionInTransitTypePtrInput {
	return (*connectorKafkaClusterEncryptionInTransitTypePtr)(&v)
}

func (*connectorKafkaClusterEncryptionInTransitTypePtr) ElementType() reflect.Type {
	return connectorKafkaClusterEncryptionInTransitTypePtrType
}

func (in *connectorKafkaClusterEncryptionInTransitTypePtr) ToConnectorKafkaClusterEncryptionInTransitTypePtrOutput() ConnectorKafkaClusterEncryptionInTransitTypePtrOutput {
	return pulumi.ToOutput(in).(ConnectorKafkaClusterEncryptionInTransitTypePtrOutput)
}

func (in *connectorKafkaClusterEncryptionInTransitTypePtr) ToConnectorKafkaClusterEncryptionInTransitTypePtrOutputWithContext(ctx context.Context) ConnectorKafkaClusterEncryptionInTransitTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(ConnectorKafkaClusterEncryptionInTransitTypePtrOutput)
}

func (in *connectorKafkaClusterEncryptionInTransitTypePtr) ToOutput(ctx context.Context) pulumix.Output[*ConnectorKafkaClusterEncryptionInTransitType] {
	return pulumix.Output[*ConnectorKafkaClusterEncryptionInTransitType]{
		OutputState: in.ToConnectorKafkaClusterEncryptionInTransitTypePtrOutputWithContext(ctx).OutputState,
	}
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ConnectorKafkaClusterClientAuthenticationTypeInput)(nil)).Elem(), ConnectorKafkaClusterClientAuthenticationType("NONE"))
	pulumi.RegisterInputType(reflect.TypeOf((*ConnectorKafkaClusterClientAuthenticationTypePtrInput)(nil)).Elem(), ConnectorKafkaClusterClientAuthenticationType("NONE"))
	pulumi.RegisterInputType(reflect.TypeOf((*ConnectorKafkaClusterEncryptionInTransitTypeInput)(nil)).Elem(), ConnectorKafkaClusterEncryptionInTransitType("PLAINTEXT"))
	pulumi.RegisterInputType(reflect.TypeOf((*ConnectorKafkaClusterEncryptionInTransitTypePtrInput)(nil)).Elem(), ConnectorKafkaClusterEncryptionInTransitType("PLAINTEXT"))
	pulumi.RegisterOutputType(ConnectorKafkaClusterClientAuthenticationTypeOutput{})
	pulumi.RegisterOutputType(ConnectorKafkaClusterClientAuthenticationTypePtrOutput{})
	pulumi.RegisterOutputType(ConnectorKafkaClusterEncryptionInTransitTypeOutput{})
	pulumi.RegisterOutputType(ConnectorKafkaClusterEncryptionInTransitTypePtrOutput{})
}

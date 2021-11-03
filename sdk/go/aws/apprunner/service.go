// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package apprunner

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::AppRunner::Service resource specifies an AppRunner Service.
type Service struct {
	pulumi.CustomResourceState

	// Autoscaling configuration ARN
	AutoScalingConfigurationArn pulumi.StringPtrOutput                   `pulumi:"autoScalingConfigurationArn"`
	EncryptionConfiguration     ServiceEncryptionConfigurationPtrOutput  `pulumi:"encryptionConfiguration"`
	HealthCheckConfiguration    ServiceHealthCheckConfigurationPtrOutput `pulumi:"healthCheckConfiguration"`
	InstanceConfiguration       ServiceInstanceConfigurationPtrOutput    `pulumi:"instanceConfiguration"`
	// The Amazon Resource Name (ARN) of the AppRunner Service.
	ServiceArn pulumi.StringOutput `pulumi:"serviceArn"`
	// The AppRunner Service Id
	ServiceId pulumi.StringOutput `pulumi:"serviceId"`
	// The AppRunner Service Name.
	ServiceName pulumi.StringPtrOutput `pulumi:"serviceName"`
	// The Service Url of the AppRunner Service.
	ServiceUrl          pulumi.StringOutput              `pulumi:"serviceUrl"`
	SourceConfiguration ServiceSourceConfigurationOutput `pulumi:"sourceConfiguration"`
	// AppRunner Service status.
	Status pulumi.StringOutput   `pulumi:"status"`
	Tags   ServiceTagArrayOutput `pulumi:"tags"`
}

// NewService registers a new resource with the given unique name, arguments, and options.
func NewService(ctx *pulumi.Context,
	name string, args *ServiceArgs, opts ...pulumi.ResourceOption) (*Service, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.SourceConfiguration == nil {
		return nil, errors.New("invalid value for required argument 'SourceConfiguration'")
	}
	var resource Service
	err := ctx.RegisterResource("aws-native:apprunner:Service", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetService gets an existing Service resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetService(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServiceState, opts ...pulumi.ResourceOption) (*Service, error) {
	var resource Service
	err := ctx.ReadResource("aws-native:apprunner:Service", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Service resources.
type serviceState struct {
}

type ServiceState struct {
}

func (ServiceState) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceState)(nil)).Elem()
}

type serviceArgs struct {
	// Autoscaling configuration ARN
	AutoScalingConfigurationArn *string                          `pulumi:"autoScalingConfigurationArn"`
	EncryptionConfiguration     *ServiceEncryptionConfiguration  `pulumi:"encryptionConfiguration"`
	HealthCheckConfiguration    *ServiceHealthCheckConfiguration `pulumi:"healthCheckConfiguration"`
	InstanceConfiguration       *ServiceInstanceConfiguration    `pulumi:"instanceConfiguration"`
	// The AppRunner Service Name.
	ServiceName         *string                    `pulumi:"serviceName"`
	SourceConfiguration ServiceSourceConfiguration `pulumi:"sourceConfiguration"`
	Tags                []ServiceTag               `pulumi:"tags"`
}

// The set of arguments for constructing a Service resource.
type ServiceArgs struct {
	// Autoscaling configuration ARN
	AutoScalingConfigurationArn pulumi.StringPtrInput
	EncryptionConfiguration     ServiceEncryptionConfigurationPtrInput
	HealthCheckConfiguration    ServiceHealthCheckConfigurationPtrInput
	InstanceConfiguration       ServiceInstanceConfigurationPtrInput
	// The AppRunner Service Name.
	ServiceName         pulumi.StringPtrInput
	SourceConfiguration ServiceSourceConfigurationInput
	Tags                ServiceTagArrayInput
}

func (ServiceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceArgs)(nil)).Elem()
}

type ServiceInput interface {
	pulumi.Input

	ToServiceOutput() ServiceOutput
	ToServiceOutputWithContext(ctx context.Context) ServiceOutput
}

func (*Service) ElementType() reflect.Type {
	return reflect.TypeOf((*Service)(nil))
}

func (i *Service) ToServiceOutput() ServiceOutput {
	return i.ToServiceOutputWithContext(context.Background())
}

func (i *Service) ToServiceOutputWithContext(ctx context.Context) ServiceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceOutput)
}

type ServiceOutput struct{ *pulumi.OutputState }

func (ServiceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Service)(nil))
}

func (o ServiceOutput) ToServiceOutput() ServiceOutput {
	return o
}

func (o ServiceOutput) ToServiceOutputWithContext(ctx context.Context) ServiceOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceInput)(nil)).Elem(), &Service{})
	pulumi.RegisterOutputType(ServiceOutput{})
}

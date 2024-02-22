// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package emrserverless

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::EMRServerless::Application Type
type Application struct {
	pulumi.CustomResourceState

	// The ID of the EMR Serverless Application.
	ApplicationId pulumi.StringOutput              `pulumi:"applicationId"`
	Architecture  ApplicationArchitecturePtrOutput `pulumi:"architecture"`
	// The Amazon Resource Name (ARN) of the EMR Serverless Application.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Configuration for Auto Start of Application.
	AutoStartConfiguration ApplicationAutoStartConfigurationPtrOutput `pulumi:"autoStartConfiguration"`
	// Configuration for Auto Stop of Application.
	AutoStopConfiguration ApplicationAutoStopConfigurationPtrOutput   `pulumi:"autoStopConfiguration"`
	ImageConfiguration    ApplicationImageConfigurationInputPtrOutput `pulumi:"imageConfiguration"`
	// Initial capacity initialized when an Application is started.
	InitialCapacity ApplicationInitialCapacityConfigKeyValuePairArrayOutput `pulumi:"initialCapacity"`
	// Maximum allowed cumulative resources for an Application. No new resources will be created once the limit is hit.
	MaximumCapacity         ApplicationMaximumAllowedResourcesPtrOutput `pulumi:"maximumCapacity"`
	MonitoringConfiguration ApplicationMonitoringConfigurationPtrOutput `pulumi:"monitoringConfiguration"`
	// User friendly Application name.
	Name pulumi.StringPtrOutput `pulumi:"name"`
	// Network Configuration for customer VPC connectivity.
	NetworkConfiguration ApplicationNetworkConfigurationPtrOutput `pulumi:"networkConfiguration"`
	// EMR release label.
	ReleaseLabel         pulumi.StringOutput                       `pulumi:"releaseLabel"`
	RuntimeConfiguration ApplicationConfigurationObjectArrayOutput `pulumi:"runtimeConfiguration"`
	// Tag map with key and value
	Tags aws.TagArrayOutput `pulumi:"tags"`
	// The type of the application
	Type pulumi.StringOutput `pulumi:"type"`
	// The key-value pairs that specify worker type to WorkerTypeSpecificationInput. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include Driver and Executor for Spark applications and HiveDriver and TezTask for Hive applications. You can either set image details in this parameter for each worker type, or in imageConfiguration for all worker types.
	WorkerTypeSpecifications ApplicationWorkerTypeSpecificationInputMapPtrOutput `pulumi:"workerTypeSpecifications"`
}

// NewApplication registers a new resource with the given unique name, arguments, and options.
func NewApplication(ctx *pulumi.Context,
	name string, args *ApplicationArgs, opts ...pulumi.ResourceOption) (*Application, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ReleaseLabel == nil {
		return nil, errors.New("invalid value for required argument 'ReleaseLabel'")
	}
	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"name",
		"type",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Application
	err := ctx.RegisterResource("aws-native:emrserverless:Application", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetApplication gets an existing Application resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetApplication(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ApplicationState, opts ...pulumi.ResourceOption) (*Application, error) {
	var resource Application
	err := ctx.ReadResource("aws-native:emrserverless:Application", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Application resources.
type applicationState struct {
}

type ApplicationState struct {
}

func (ApplicationState) ElementType() reflect.Type {
	return reflect.TypeOf((*applicationState)(nil)).Elem()
}

type applicationArgs struct {
	Architecture *ApplicationArchitecture `pulumi:"architecture"`
	// Configuration for Auto Start of Application.
	AutoStartConfiguration *ApplicationAutoStartConfiguration `pulumi:"autoStartConfiguration"`
	// Configuration for Auto Stop of Application.
	AutoStopConfiguration *ApplicationAutoStopConfiguration   `pulumi:"autoStopConfiguration"`
	ImageConfiguration    *ApplicationImageConfigurationInput `pulumi:"imageConfiguration"`
	// Initial capacity initialized when an Application is started.
	InitialCapacity []ApplicationInitialCapacityConfigKeyValuePair `pulumi:"initialCapacity"`
	// Maximum allowed cumulative resources for an Application. No new resources will be created once the limit is hit.
	MaximumCapacity         *ApplicationMaximumAllowedResources `pulumi:"maximumCapacity"`
	MonitoringConfiguration *ApplicationMonitoringConfiguration `pulumi:"monitoringConfiguration"`
	// User friendly Application name.
	Name *string `pulumi:"name"`
	// Network Configuration for customer VPC connectivity.
	NetworkConfiguration *ApplicationNetworkConfiguration `pulumi:"networkConfiguration"`
	// EMR release label.
	ReleaseLabel         string                           `pulumi:"releaseLabel"`
	RuntimeConfiguration []ApplicationConfigurationObject `pulumi:"runtimeConfiguration"`
	// Tag map with key and value
	Tags []aws.Tag `pulumi:"tags"`
	// The type of the application
	Type string `pulumi:"type"`
	// The key-value pairs that specify worker type to WorkerTypeSpecificationInput. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include Driver and Executor for Spark applications and HiveDriver and TezTask for Hive applications. You can either set image details in this parameter for each worker type, or in imageConfiguration for all worker types.
	WorkerTypeSpecifications *ApplicationWorkerTypeSpecificationInputMap `pulumi:"workerTypeSpecifications"`
}

// The set of arguments for constructing a Application resource.
type ApplicationArgs struct {
	Architecture ApplicationArchitecturePtrInput
	// Configuration for Auto Start of Application.
	AutoStartConfiguration ApplicationAutoStartConfigurationPtrInput
	// Configuration for Auto Stop of Application.
	AutoStopConfiguration ApplicationAutoStopConfigurationPtrInput
	ImageConfiguration    ApplicationImageConfigurationInputPtrInput
	// Initial capacity initialized when an Application is started.
	InitialCapacity ApplicationInitialCapacityConfigKeyValuePairArrayInput
	// Maximum allowed cumulative resources for an Application. No new resources will be created once the limit is hit.
	MaximumCapacity         ApplicationMaximumAllowedResourcesPtrInput
	MonitoringConfiguration ApplicationMonitoringConfigurationPtrInput
	// User friendly Application name.
	Name pulumi.StringPtrInput
	// Network Configuration for customer VPC connectivity.
	NetworkConfiguration ApplicationNetworkConfigurationPtrInput
	// EMR release label.
	ReleaseLabel         pulumi.StringInput
	RuntimeConfiguration ApplicationConfigurationObjectArrayInput
	// Tag map with key and value
	Tags aws.TagArrayInput
	// The type of the application
	Type pulumi.StringInput
	// The key-value pairs that specify worker type to WorkerTypeSpecificationInput. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include Driver and Executor for Spark applications and HiveDriver and TezTask for Hive applications. You can either set image details in this parameter for each worker type, or in imageConfiguration for all worker types.
	WorkerTypeSpecifications ApplicationWorkerTypeSpecificationInputMapPtrInput
}

func (ApplicationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*applicationArgs)(nil)).Elem()
}

type ApplicationInput interface {
	pulumi.Input

	ToApplicationOutput() ApplicationOutput
	ToApplicationOutputWithContext(ctx context.Context) ApplicationOutput
}

func (*Application) ElementType() reflect.Type {
	return reflect.TypeOf((**Application)(nil)).Elem()
}

func (i *Application) ToApplicationOutput() ApplicationOutput {
	return i.ToApplicationOutputWithContext(context.Background())
}

func (i *Application) ToApplicationOutputWithContext(ctx context.Context) ApplicationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ApplicationOutput)
}

type ApplicationOutput struct{ *pulumi.OutputState }

func (ApplicationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Application)(nil)).Elem()
}

func (o ApplicationOutput) ToApplicationOutput() ApplicationOutput {
	return o
}

func (o ApplicationOutput) ToApplicationOutputWithContext(ctx context.Context) ApplicationOutput {
	return o
}

// The ID of the EMR Serverless Application.
func (o ApplicationOutput) ApplicationId() pulumi.StringOutput {
	return o.ApplyT(func(v *Application) pulumi.StringOutput { return v.ApplicationId }).(pulumi.StringOutput)
}

func (o ApplicationOutput) Architecture() ApplicationArchitecturePtrOutput {
	return o.ApplyT(func(v *Application) ApplicationArchitecturePtrOutput { return v.Architecture }).(ApplicationArchitecturePtrOutput)
}

// The Amazon Resource Name (ARN) of the EMR Serverless Application.
func (o ApplicationOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Application) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// Configuration for Auto Start of Application.
func (o ApplicationOutput) AutoStartConfiguration() ApplicationAutoStartConfigurationPtrOutput {
	return o.ApplyT(func(v *Application) ApplicationAutoStartConfigurationPtrOutput { return v.AutoStartConfiguration }).(ApplicationAutoStartConfigurationPtrOutput)
}

// Configuration for Auto Stop of Application.
func (o ApplicationOutput) AutoStopConfiguration() ApplicationAutoStopConfigurationPtrOutput {
	return o.ApplyT(func(v *Application) ApplicationAutoStopConfigurationPtrOutput { return v.AutoStopConfiguration }).(ApplicationAutoStopConfigurationPtrOutput)
}

func (o ApplicationOutput) ImageConfiguration() ApplicationImageConfigurationInputPtrOutput {
	return o.ApplyT(func(v *Application) ApplicationImageConfigurationInputPtrOutput { return v.ImageConfiguration }).(ApplicationImageConfigurationInputPtrOutput)
}

// Initial capacity initialized when an Application is started.
func (o ApplicationOutput) InitialCapacity() ApplicationInitialCapacityConfigKeyValuePairArrayOutput {
	return o.ApplyT(func(v *Application) ApplicationInitialCapacityConfigKeyValuePairArrayOutput { return v.InitialCapacity }).(ApplicationInitialCapacityConfigKeyValuePairArrayOutput)
}

// Maximum allowed cumulative resources for an Application. No new resources will be created once the limit is hit.
func (o ApplicationOutput) MaximumCapacity() ApplicationMaximumAllowedResourcesPtrOutput {
	return o.ApplyT(func(v *Application) ApplicationMaximumAllowedResourcesPtrOutput { return v.MaximumCapacity }).(ApplicationMaximumAllowedResourcesPtrOutput)
}

func (o ApplicationOutput) MonitoringConfiguration() ApplicationMonitoringConfigurationPtrOutput {
	return o.ApplyT(func(v *Application) ApplicationMonitoringConfigurationPtrOutput { return v.MonitoringConfiguration }).(ApplicationMonitoringConfigurationPtrOutput)
}

// User friendly Application name.
func (o ApplicationOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Application) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

// Network Configuration for customer VPC connectivity.
func (o ApplicationOutput) NetworkConfiguration() ApplicationNetworkConfigurationPtrOutput {
	return o.ApplyT(func(v *Application) ApplicationNetworkConfigurationPtrOutput { return v.NetworkConfiguration }).(ApplicationNetworkConfigurationPtrOutput)
}

// EMR release label.
func (o ApplicationOutput) ReleaseLabel() pulumi.StringOutput {
	return o.ApplyT(func(v *Application) pulumi.StringOutput { return v.ReleaseLabel }).(pulumi.StringOutput)
}

func (o ApplicationOutput) RuntimeConfiguration() ApplicationConfigurationObjectArrayOutput {
	return o.ApplyT(func(v *Application) ApplicationConfigurationObjectArrayOutput { return v.RuntimeConfiguration }).(ApplicationConfigurationObjectArrayOutput)
}

// Tag map with key and value
func (o ApplicationOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *Application) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

// The type of the application
func (o ApplicationOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *Application) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

// The key-value pairs that specify worker type to WorkerTypeSpecificationInput. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include Driver and Executor for Spark applications and HiveDriver and TezTask for Hive applications. You can either set image details in this parameter for each worker type, or in imageConfiguration for all worker types.
func (o ApplicationOutput) WorkerTypeSpecifications() ApplicationWorkerTypeSpecificationInputMapPtrOutput {
	return o.ApplyT(func(v *Application) ApplicationWorkerTypeSpecificationInputMapPtrOutput {
		return v.WorkerTypeSpecifications
	}).(ApplicationWorkerTypeSpecificationInputMapPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ApplicationInput)(nil)).Elem(), &Application{})
	pulumi.RegisterOutputType(ApplicationOutput{})
}

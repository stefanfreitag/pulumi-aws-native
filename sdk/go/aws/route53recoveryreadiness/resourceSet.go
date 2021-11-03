// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package route53recoveryreadiness

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Schema for the AWS Route53 Recovery Readiness ResourceSet Resource and API.
type ResourceSet struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) of the resource set.
	ResourceSetArn pulumi.StringOutput `pulumi:"resourceSetArn"`
	// The name of the resource set to create.
	ResourceSetName pulumi.StringOutput `pulumi:"resourceSetName"`
	// The resource type of the resources in the resource set. Enter one of the following values for resource type:
	//
	// AWS: :AutoScaling: :AutoScalingGroup, AWS: :CloudWatch: :Alarm, AWS: :EC2: :CustomerGateway, AWS: :DynamoDB: :Table, AWS: :EC2: :Volume, AWS: :ElasticLoadBalancing: :LoadBalancer, AWS: :ElasticLoadBalancingV2: :LoadBalancer, AWS: :MSK: :Cluster, AWS: :RDS: :DBCluster, AWS: :Route53: :HealthCheck, AWS: :SQS: :Queue, AWS: :SNS: :Topic, AWS: :SNS: :Subscription, AWS: :EC2: :VPC, AWS: :EC2: :VPNConnection, AWS: :EC2: :VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource
	ResourceSetType pulumi.StringOutput `pulumi:"resourceSetType"`
	// A list of resource objects in the resource set.
	Resources ResourceSetResourceArrayOutput `pulumi:"resources"`
	// A tag to associate with the parameters for a resource set.
	Tags ResourceSetTagArrayOutput `pulumi:"tags"`
}

// NewResourceSet registers a new resource with the given unique name, arguments, and options.
func NewResourceSet(ctx *pulumi.Context,
	name string, args *ResourceSetArgs, opts ...pulumi.ResourceOption) (*ResourceSet, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ResourceSetName == nil {
		return nil, errors.New("invalid value for required argument 'ResourceSetName'")
	}
	if args.ResourceSetType == nil {
		return nil, errors.New("invalid value for required argument 'ResourceSetType'")
	}
	if args.Resources == nil {
		return nil, errors.New("invalid value for required argument 'Resources'")
	}
	var resource ResourceSet
	err := ctx.RegisterResource("aws-native:route53recoveryreadiness:ResourceSet", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetResourceSet gets an existing ResourceSet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetResourceSet(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ResourceSetState, opts ...pulumi.ResourceOption) (*ResourceSet, error) {
	var resource ResourceSet
	err := ctx.ReadResource("aws-native:route53recoveryreadiness:ResourceSet", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ResourceSet resources.
type resourceSetState struct {
}

type ResourceSetState struct {
}

func (ResourceSetState) ElementType() reflect.Type {
	return reflect.TypeOf((*resourceSetState)(nil)).Elem()
}

type resourceSetArgs struct {
	// The name of the resource set to create.
	ResourceSetName string `pulumi:"resourceSetName"`
	// The resource type of the resources in the resource set. Enter one of the following values for resource type:
	//
	// AWS: :AutoScaling: :AutoScalingGroup, AWS: :CloudWatch: :Alarm, AWS: :EC2: :CustomerGateway, AWS: :DynamoDB: :Table, AWS: :EC2: :Volume, AWS: :ElasticLoadBalancing: :LoadBalancer, AWS: :ElasticLoadBalancingV2: :LoadBalancer, AWS: :MSK: :Cluster, AWS: :RDS: :DBCluster, AWS: :Route53: :HealthCheck, AWS: :SQS: :Queue, AWS: :SNS: :Topic, AWS: :SNS: :Subscription, AWS: :EC2: :VPC, AWS: :EC2: :VPNConnection, AWS: :EC2: :VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource
	ResourceSetType string `pulumi:"resourceSetType"`
	// A list of resource objects in the resource set.
	Resources []ResourceSetResource `pulumi:"resources"`
	// A tag to associate with the parameters for a resource set.
	Tags []ResourceSetTag `pulumi:"tags"`
}

// The set of arguments for constructing a ResourceSet resource.
type ResourceSetArgs struct {
	// The name of the resource set to create.
	ResourceSetName pulumi.StringInput
	// The resource type of the resources in the resource set. Enter one of the following values for resource type:
	//
	// AWS: :AutoScaling: :AutoScalingGroup, AWS: :CloudWatch: :Alarm, AWS: :EC2: :CustomerGateway, AWS: :DynamoDB: :Table, AWS: :EC2: :Volume, AWS: :ElasticLoadBalancing: :LoadBalancer, AWS: :ElasticLoadBalancingV2: :LoadBalancer, AWS: :MSK: :Cluster, AWS: :RDS: :DBCluster, AWS: :Route53: :HealthCheck, AWS: :SQS: :Queue, AWS: :SNS: :Topic, AWS: :SNS: :Subscription, AWS: :EC2: :VPC, AWS: :EC2: :VPNConnection, AWS: :EC2: :VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource
	ResourceSetType pulumi.StringInput
	// A list of resource objects in the resource set.
	Resources ResourceSetResourceArrayInput
	// A tag to associate with the parameters for a resource set.
	Tags ResourceSetTagArrayInput
}

func (ResourceSetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*resourceSetArgs)(nil)).Elem()
}

type ResourceSetInput interface {
	pulumi.Input

	ToResourceSetOutput() ResourceSetOutput
	ToResourceSetOutputWithContext(ctx context.Context) ResourceSetOutput
}

func (*ResourceSet) ElementType() reflect.Type {
	return reflect.TypeOf((*ResourceSet)(nil))
}

func (i *ResourceSet) ToResourceSetOutput() ResourceSetOutput {
	return i.ToResourceSetOutputWithContext(context.Background())
}

func (i *ResourceSet) ToResourceSetOutputWithContext(ctx context.Context) ResourceSetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ResourceSetOutput)
}

type ResourceSetOutput struct{ *pulumi.OutputState }

func (ResourceSetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ResourceSet)(nil))
}

func (o ResourceSetOutput) ToResourceSetOutput() ResourceSetOutput {
	return o
}

func (o ResourceSetOutput) ToResourceSetOutputWithContext(ctx context.Context) ResourceSetOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ResourceSetInput)(nil)).Elem(), &ResourceSet{})
	pulumi.RegisterOutputType(ResourceSetOutput{})
}

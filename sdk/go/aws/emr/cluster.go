// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package emr

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::EMR::Cluster
//
// Deprecated: Cluster is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Cluster struct {
	pulumi.CustomResourceState

	AdditionalInfo        pulumi.AnyOutput                        `pulumi:"additionalInfo"`
	Applications          ClusterApplicationArrayOutput           `pulumi:"applications"`
	AutoScalingRole       pulumi.StringPtrOutput                  `pulumi:"autoScalingRole"`
	AutoTerminationPolicy ClusterAutoTerminationPolicyPtrOutput   `pulumi:"autoTerminationPolicy"`
	BootstrapActions      ClusterBootstrapActionConfigArrayOutput `pulumi:"bootstrapActions"`
	Configurations        ClusterConfigurationArrayOutput         `pulumi:"configurations"`
	CustomAmiId           pulumi.StringPtrOutput                  `pulumi:"customAmiId"`
	EbsRootVolumeSize     pulumi.IntPtrOutput                     `pulumi:"ebsRootVolumeSize"`
	Instances             ClusterJobFlowInstancesConfigOutput     `pulumi:"instances"`
	JobFlowRole           pulumi.StringOutput                     `pulumi:"jobFlowRole"`
	KerberosAttributes    ClusterKerberosAttributesPtrOutput      `pulumi:"kerberosAttributes"`
	LogEncryptionKmsKeyId pulumi.StringPtrOutput                  `pulumi:"logEncryptionKmsKeyId"`
	LogUri                pulumi.StringPtrOutput                  `pulumi:"logUri"`
	ManagedScalingPolicy  ClusterManagedScalingPolicyPtrOutput    `pulumi:"managedScalingPolicy"`
	MasterPublicDns       pulumi.StringOutput                     `pulumi:"masterPublicDns"`
	Name                  pulumi.StringOutput                     `pulumi:"name"`
	OsReleaseLabel        pulumi.StringPtrOutput                  `pulumi:"osReleaseLabel"`
	ReleaseLabel          pulumi.StringPtrOutput                  `pulumi:"releaseLabel"`
	ScaleDownBehavior     pulumi.StringPtrOutput                  `pulumi:"scaleDownBehavior"`
	SecurityConfiguration pulumi.StringPtrOutput                  `pulumi:"securityConfiguration"`
	ServiceRole           pulumi.StringOutput                     `pulumi:"serviceRole"`
	StepConcurrencyLevel  pulumi.IntPtrOutput                     `pulumi:"stepConcurrencyLevel"`
	Steps                 ClusterStepConfigArrayOutput            `pulumi:"steps"`
	Tags                  ClusterTagArrayOutput                   `pulumi:"tags"`
	VisibleToAllUsers     pulumi.BoolPtrOutput                    `pulumi:"visibleToAllUsers"`
}

// NewCluster registers a new resource with the given unique name, arguments, and options.
func NewCluster(ctx *pulumi.Context,
	name string, args *ClusterArgs, opts ...pulumi.ResourceOption) (*Cluster, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Instances == nil {
		return nil, errors.New("invalid value for required argument 'Instances'")
	}
	if args.JobFlowRole == nil {
		return nil, errors.New("invalid value for required argument 'JobFlowRole'")
	}
	if args.ServiceRole == nil {
		return nil, errors.New("invalid value for required argument 'ServiceRole'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"additionalInfo",
		"applications[*]",
		"autoScalingRole",
		"bootstrapActions[*]",
		"configurations[*]",
		"customAmiId",
		"ebsRootVolumeSize",
		"jobFlowRole",
		"kerberosAttributes",
		"logEncryptionKmsKeyId",
		"logUri",
		"name",
		"osReleaseLabel",
		"releaseLabel",
		"scaleDownBehavior",
		"securityConfiguration",
		"serviceRole",
		"steps[*]",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Cluster
	err := ctx.RegisterResource("aws-native:emr:Cluster", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCluster gets an existing Cluster resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCluster(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ClusterState, opts ...pulumi.ResourceOption) (*Cluster, error) {
	var resource Cluster
	err := ctx.ReadResource("aws-native:emr:Cluster", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Cluster resources.
type clusterState struct {
}

type ClusterState struct {
}

func (ClusterState) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterState)(nil)).Elem()
}

type clusterArgs struct {
	AdditionalInfo        interface{}                    `pulumi:"additionalInfo"`
	Applications          []ClusterApplication           `pulumi:"applications"`
	AutoScalingRole       *string                        `pulumi:"autoScalingRole"`
	AutoTerminationPolicy *ClusterAutoTerminationPolicy  `pulumi:"autoTerminationPolicy"`
	BootstrapActions      []ClusterBootstrapActionConfig `pulumi:"bootstrapActions"`
	Configurations        []ClusterConfiguration         `pulumi:"configurations"`
	CustomAmiId           *string                        `pulumi:"customAmiId"`
	EbsRootVolumeSize     *int                           `pulumi:"ebsRootVolumeSize"`
	Instances             ClusterJobFlowInstancesConfig  `pulumi:"instances"`
	JobFlowRole           string                         `pulumi:"jobFlowRole"`
	KerberosAttributes    *ClusterKerberosAttributes     `pulumi:"kerberosAttributes"`
	LogEncryptionKmsKeyId *string                        `pulumi:"logEncryptionKmsKeyId"`
	LogUri                *string                        `pulumi:"logUri"`
	ManagedScalingPolicy  *ClusterManagedScalingPolicy   `pulumi:"managedScalingPolicy"`
	Name                  *string                        `pulumi:"name"`
	OsReleaseLabel        *string                        `pulumi:"osReleaseLabel"`
	ReleaseLabel          *string                        `pulumi:"releaseLabel"`
	ScaleDownBehavior     *string                        `pulumi:"scaleDownBehavior"`
	SecurityConfiguration *string                        `pulumi:"securityConfiguration"`
	ServiceRole           string                         `pulumi:"serviceRole"`
	StepConcurrencyLevel  *int                           `pulumi:"stepConcurrencyLevel"`
	Steps                 []ClusterStepConfig            `pulumi:"steps"`
	Tags                  []ClusterTag                   `pulumi:"tags"`
	VisibleToAllUsers     *bool                          `pulumi:"visibleToAllUsers"`
}

// The set of arguments for constructing a Cluster resource.
type ClusterArgs struct {
	AdditionalInfo        pulumi.Input
	Applications          ClusterApplicationArrayInput
	AutoScalingRole       pulumi.StringPtrInput
	AutoTerminationPolicy ClusterAutoTerminationPolicyPtrInput
	BootstrapActions      ClusterBootstrapActionConfigArrayInput
	Configurations        ClusterConfigurationArrayInput
	CustomAmiId           pulumi.StringPtrInput
	EbsRootVolumeSize     pulumi.IntPtrInput
	Instances             ClusterJobFlowInstancesConfigInput
	JobFlowRole           pulumi.StringInput
	KerberosAttributes    ClusterKerberosAttributesPtrInput
	LogEncryptionKmsKeyId pulumi.StringPtrInput
	LogUri                pulumi.StringPtrInput
	ManagedScalingPolicy  ClusterManagedScalingPolicyPtrInput
	Name                  pulumi.StringPtrInput
	OsReleaseLabel        pulumi.StringPtrInput
	ReleaseLabel          pulumi.StringPtrInput
	ScaleDownBehavior     pulumi.StringPtrInput
	SecurityConfiguration pulumi.StringPtrInput
	ServiceRole           pulumi.StringInput
	StepConcurrencyLevel  pulumi.IntPtrInput
	Steps                 ClusterStepConfigArrayInput
	Tags                  ClusterTagArrayInput
	VisibleToAllUsers     pulumi.BoolPtrInput
}

func (ClusterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterArgs)(nil)).Elem()
}

type ClusterInput interface {
	pulumi.Input

	ToClusterOutput() ClusterOutput
	ToClusterOutputWithContext(ctx context.Context) ClusterOutput
}

func (*Cluster) ElementType() reflect.Type {
	return reflect.TypeOf((**Cluster)(nil)).Elem()
}

func (i *Cluster) ToClusterOutput() ClusterOutput {
	return i.ToClusterOutputWithContext(context.Background())
}

func (i *Cluster) ToClusterOutputWithContext(ctx context.Context) ClusterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterOutput)
}

func (i *Cluster) ToOutput(ctx context.Context) pulumix.Output[*Cluster] {
	return pulumix.Output[*Cluster]{
		OutputState: i.ToClusterOutputWithContext(ctx).OutputState,
	}
}

type ClusterOutput struct{ *pulumi.OutputState }

func (ClusterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Cluster)(nil)).Elem()
}

func (o ClusterOutput) ToClusterOutput() ClusterOutput {
	return o
}

func (o ClusterOutput) ToClusterOutputWithContext(ctx context.Context) ClusterOutput {
	return o
}

func (o ClusterOutput) ToOutput(ctx context.Context) pulumix.Output[*Cluster] {
	return pulumix.Output[*Cluster]{
		OutputState: o.OutputState,
	}
}

func (o ClusterOutput) AdditionalInfo() pulumi.AnyOutput {
	return o.ApplyT(func(v *Cluster) pulumi.AnyOutput { return v.AdditionalInfo }).(pulumi.AnyOutput)
}

func (o ClusterOutput) Applications() ClusterApplicationArrayOutput {
	return o.ApplyT(func(v *Cluster) ClusterApplicationArrayOutput { return v.Applications }).(ClusterApplicationArrayOutput)
}

func (o ClusterOutput) AutoScalingRole() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Cluster) pulumi.StringPtrOutput { return v.AutoScalingRole }).(pulumi.StringPtrOutput)
}

func (o ClusterOutput) AutoTerminationPolicy() ClusterAutoTerminationPolicyPtrOutput {
	return o.ApplyT(func(v *Cluster) ClusterAutoTerminationPolicyPtrOutput { return v.AutoTerminationPolicy }).(ClusterAutoTerminationPolicyPtrOutput)
}

func (o ClusterOutput) BootstrapActions() ClusterBootstrapActionConfigArrayOutput {
	return o.ApplyT(func(v *Cluster) ClusterBootstrapActionConfigArrayOutput { return v.BootstrapActions }).(ClusterBootstrapActionConfigArrayOutput)
}

func (o ClusterOutput) Configurations() ClusterConfigurationArrayOutput {
	return o.ApplyT(func(v *Cluster) ClusterConfigurationArrayOutput { return v.Configurations }).(ClusterConfigurationArrayOutput)
}

func (o ClusterOutput) CustomAmiId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Cluster) pulumi.StringPtrOutput { return v.CustomAmiId }).(pulumi.StringPtrOutput)
}

func (o ClusterOutput) EbsRootVolumeSize() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Cluster) pulumi.IntPtrOutput { return v.EbsRootVolumeSize }).(pulumi.IntPtrOutput)
}

func (o ClusterOutput) Instances() ClusterJobFlowInstancesConfigOutput {
	return o.ApplyT(func(v *Cluster) ClusterJobFlowInstancesConfigOutput { return v.Instances }).(ClusterJobFlowInstancesConfigOutput)
}

func (o ClusterOutput) JobFlowRole() pulumi.StringOutput {
	return o.ApplyT(func(v *Cluster) pulumi.StringOutput { return v.JobFlowRole }).(pulumi.StringOutput)
}

func (o ClusterOutput) KerberosAttributes() ClusterKerberosAttributesPtrOutput {
	return o.ApplyT(func(v *Cluster) ClusterKerberosAttributesPtrOutput { return v.KerberosAttributes }).(ClusterKerberosAttributesPtrOutput)
}

func (o ClusterOutput) LogEncryptionKmsKeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Cluster) pulumi.StringPtrOutput { return v.LogEncryptionKmsKeyId }).(pulumi.StringPtrOutput)
}

func (o ClusterOutput) LogUri() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Cluster) pulumi.StringPtrOutput { return v.LogUri }).(pulumi.StringPtrOutput)
}

func (o ClusterOutput) ManagedScalingPolicy() ClusterManagedScalingPolicyPtrOutput {
	return o.ApplyT(func(v *Cluster) ClusterManagedScalingPolicyPtrOutput { return v.ManagedScalingPolicy }).(ClusterManagedScalingPolicyPtrOutput)
}

func (o ClusterOutput) MasterPublicDns() pulumi.StringOutput {
	return o.ApplyT(func(v *Cluster) pulumi.StringOutput { return v.MasterPublicDns }).(pulumi.StringOutput)
}

func (o ClusterOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Cluster) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o ClusterOutput) OsReleaseLabel() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Cluster) pulumi.StringPtrOutput { return v.OsReleaseLabel }).(pulumi.StringPtrOutput)
}

func (o ClusterOutput) ReleaseLabel() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Cluster) pulumi.StringPtrOutput { return v.ReleaseLabel }).(pulumi.StringPtrOutput)
}

func (o ClusterOutput) ScaleDownBehavior() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Cluster) pulumi.StringPtrOutput { return v.ScaleDownBehavior }).(pulumi.StringPtrOutput)
}

func (o ClusterOutput) SecurityConfiguration() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Cluster) pulumi.StringPtrOutput { return v.SecurityConfiguration }).(pulumi.StringPtrOutput)
}

func (o ClusterOutput) ServiceRole() pulumi.StringOutput {
	return o.ApplyT(func(v *Cluster) pulumi.StringOutput { return v.ServiceRole }).(pulumi.StringOutput)
}

func (o ClusterOutput) StepConcurrencyLevel() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Cluster) pulumi.IntPtrOutput { return v.StepConcurrencyLevel }).(pulumi.IntPtrOutput)
}

func (o ClusterOutput) Steps() ClusterStepConfigArrayOutput {
	return o.ApplyT(func(v *Cluster) ClusterStepConfigArrayOutput { return v.Steps }).(ClusterStepConfigArrayOutput)
}

func (o ClusterOutput) Tags() ClusterTagArrayOutput {
	return o.ApplyT(func(v *Cluster) ClusterTagArrayOutput { return v.Tags }).(ClusterTagArrayOutput)
}

func (o ClusterOutput) VisibleToAllUsers() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Cluster) pulumi.BoolPtrOutput { return v.VisibleToAllUsers }).(pulumi.BoolPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ClusterInput)(nil)).Elem(), &Cluster{})
	pulumi.RegisterOutputType(ClusterOutput{})
}

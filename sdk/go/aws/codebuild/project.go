// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package codebuild

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::CodeBuild::Project
//
// Deprecated: Project is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Project struct {
	pulumi.CustomResourceState

	Arn                     pulumi.StringOutput                  `pulumi:"arn"`
	Artifacts               ProjectArtifactsOutput               `pulumi:"artifacts"`
	BadgeEnabled            pulumi.BoolPtrOutput                 `pulumi:"badgeEnabled"`
	BuildBatchConfig        ProjectBuildBatchConfigPtrOutput     `pulumi:"buildBatchConfig"`
	Cache                   ProjectCachePtrOutput                `pulumi:"cache"`
	ConcurrentBuildLimit    pulumi.IntPtrOutput                  `pulumi:"concurrentBuildLimit"`
	Description             pulumi.StringPtrOutput               `pulumi:"description"`
	EncryptionKey           pulumi.StringPtrOutput               `pulumi:"encryptionKey"`
	Environment             ProjectEnvironmentOutput             `pulumi:"environment"`
	FileSystemLocations     ProjectFileSystemLocationArrayOutput `pulumi:"fileSystemLocations"`
	LogsConfig              ProjectLogsConfigPtrOutput           `pulumi:"logsConfig"`
	Name                    pulumi.StringPtrOutput               `pulumi:"name"`
	QueuedTimeoutInMinutes  pulumi.IntPtrOutput                  `pulumi:"queuedTimeoutInMinutes"`
	ResourceAccessRole      pulumi.StringPtrOutput               `pulumi:"resourceAccessRole"`
	SecondaryArtifacts      ProjectArtifactsArrayOutput          `pulumi:"secondaryArtifacts"`
	SecondarySourceVersions ProjectSourceVersionArrayOutput      `pulumi:"secondarySourceVersions"`
	SecondarySources        ProjectSourceArrayOutput             `pulumi:"secondarySources"`
	ServiceRole             pulumi.StringOutput                  `pulumi:"serviceRole"`
	Source                  ProjectSourceOutput                  `pulumi:"source"`
	SourceVersion           pulumi.StringPtrOutput               `pulumi:"sourceVersion"`
	Tags                    ProjectTagArrayOutput                `pulumi:"tags"`
	TimeoutInMinutes        pulumi.IntPtrOutput                  `pulumi:"timeoutInMinutes"`
	Triggers                ProjectTriggersPtrOutput             `pulumi:"triggers"`
	Visibility              pulumi.StringPtrOutput               `pulumi:"visibility"`
	VpcConfig               ProjectVpcConfigPtrOutput            `pulumi:"vpcConfig"`
}

// NewProject registers a new resource with the given unique name, arguments, and options.
func NewProject(ctx *pulumi.Context,
	name string, args *ProjectArgs, opts ...pulumi.ResourceOption) (*Project, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Artifacts == nil {
		return nil, errors.New("invalid value for required argument 'Artifacts'")
	}
	if args.Environment == nil {
		return nil, errors.New("invalid value for required argument 'Environment'")
	}
	if args.ServiceRole == nil {
		return nil, errors.New("invalid value for required argument 'ServiceRole'")
	}
	if args.Source == nil {
		return nil, errors.New("invalid value for required argument 'Source'")
	}
	var resource Project
	err := ctx.RegisterResource("aws-native:codebuild:Project", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetProject gets an existing Project resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetProject(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ProjectState, opts ...pulumi.ResourceOption) (*Project, error) {
	var resource Project
	err := ctx.ReadResource("aws-native:codebuild:Project", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Project resources.
type projectState struct {
}

type ProjectState struct {
}

func (ProjectState) ElementType() reflect.Type {
	return reflect.TypeOf((*projectState)(nil)).Elem()
}

type projectArgs struct {
	Artifacts               ProjectArtifacts            `pulumi:"artifacts"`
	BadgeEnabled            *bool                       `pulumi:"badgeEnabled"`
	BuildBatchConfig        *ProjectBuildBatchConfig    `pulumi:"buildBatchConfig"`
	Cache                   *ProjectCache               `pulumi:"cache"`
	ConcurrentBuildLimit    *int                        `pulumi:"concurrentBuildLimit"`
	Description             *string                     `pulumi:"description"`
	EncryptionKey           *string                     `pulumi:"encryptionKey"`
	Environment             ProjectEnvironment          `pulumi:"environment"`
	FileSystemLocations     []ProjectFileSystemLocation `pulumi:"fileSystemLocations"`
	LogsConfig              *ProjectLogsConfig          `pulumi:"logsConfig"`
	Name                    *string                     `pulumi:"name"`
	QueuedTimeoutInMinutes  *int                        `pulumi:"queuedTimeoutInMinutes"`
	ResourceAccessRole      *string                     `pulumi:"resourceAccessRole"`
	SecondaryArtifacts      []ProjectArtifacts          `pulumi:"secondaryArtifacts"`
	SecondarySourceVersions []ProjectSourceVersion      `pulumi:"secondarySourceVersions"`
	SecondarySources        []ProjectSource             `pulumi:"secondarySources"`
	ServiceRole             string                      `pulumi:"serviceRole"`
	Source                  ProjectSource               `pulumi:"source"`
	SourceVersion           *string                     `pulumi:"sourceVersion"`
	Tags                    []ProjectTag                `pulumi:"tags"`
	TimeoutInMinutes        *int                        `pulumi:"timeoutInMinutes"`
	Triggers                *ProjectTriggers            `pulumi:"triggers"`
	Visibility              *string                     `pulumi:"visibility"`
	VpcConfig               *ProjectVpcConfig           `pulumi:"vpcConfig"`
}

// The set of arguments for constructing a Project resource.
type ProjectArgs struct {
	Artifacts               ProjectArtifactsInput
	BadgeEnabled            pulumi.BoolPtrInput
	BuildBatchConfig        ProjectBuildBatchConfigPtrInput
	Cache                   ProjectCachePtrInput
	ConcurrentBuildLimit    pulumi.IntPtrInput
	Description             pulumi.StringPtrInput
	EncryptionKey           pulumi.StringPtrInput
	Environment             ProjectEnvironmentInput
	FileSystemLocations     ProjectFileSystemLocationArrayInput
	LogsConfig              ProjectLogsConfigPtrInput
	Name                    pulumi.StringPtrInput
	QueuedTimeoutInMinutes  pulumi.IntPtrInput
	ResourceAccessRole      pulumi.StringPtrInput
	SecondaryArtifacts      ProjectArtifactsArrayInput
	SecondarySourceVersions ProjectSourceVersionArrayInput
	SecondarySources        ProjectSourceArrayInput
	ServiceRole             pulumi.StringInput
	Source                  ProjectSourceInput
	SourceVersion           pulumi.StringPtrInput
	Tags                    ProjectTagArrayInput
	TimeoutInMinutes        pulumi.IntPtrInput
	Triggers                ProjectTriggersPtrInput
	Visibility              pulumi.StringPtrInput
	VpcConfig               ProjectVpcConfigPtrInput
}

func (ProjectArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*projectArgs)(nil)).Elem()
}

type ProjectInput interface {
	pulumi.Input

	ToProjectOutput() ProjectOutput
	ToProjectOutputWithContext(ctx context.Context) ProjectOutput
}

func (*Project) ElementType() reflect.Type {
	return reflect.TypeOf((*Project)(nil))
}

func (i *Project) ToProjectOutput() ProjectOutput {
	return i.ToProjectOutputWithContext(context.Background())
}

func (i *Project) ToProjectOutputWithContext(ctx context.Context) ProjectOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProjectOutput)
}

type ProjectOutput struct{ *pulumi.OutputState }

func (ProjectOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Project)(nil))
}

func (o ProjectOutput) ToProjectOutput() ProjectOutput {
	return o
}

func (o ProjectOutput) ToProjectOutputWithContext(ctx context.Context) ProjectOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ProjectInput)(nil)).Elem(), &Project{})
	pulumi.RegisterOutputType(ProjectOutput{})
}

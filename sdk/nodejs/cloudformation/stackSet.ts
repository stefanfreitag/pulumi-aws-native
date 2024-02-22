// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * StackSet as a resource provides one-click experience for provisioning a StackSet and StackInstances
 */
export class StackSet extends pulumi.CustomResource {
    /**
     * Get an existing StackSet resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): StackSet {
        return new StackSet(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:cloudformation:StackSet';

    /**
     * Returns true if the given object is an instance of StackSet.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is StackSet {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === StackSet.__pulumiType;
    }

    /**
     * The Amazon Resource Number (ARN) of the IAM role to use to create this stack set. Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account.
     */
    public readonly administrationRoleArn!: pulumi.Output<string | undefined>;
    /**
     * Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to the target organization or organizational unit (OU). Specify only if PermissionModel is SERVICE_MANAGED.
     */
    public readonly autoDeployment!: pulumi.Output<outputs.cloudformation.StackSetAutoDeployment | undefined>;
    /**
     * Specifies the AWS account that you are acting from. By default, SELF is specified. For self-managed permissions, specify SELF; for service-managed permissions, if you are signed in to the organization's management account, specify SELF. If you are signed in to a delegated administrator account, specify DELEGATED_ADMIN.
     */
    public readonly callAs!: pulumi.Output<enums.cloudformation.StackSetCallAs | undefined>;
    /**
     * In some cases, you must explicitly acknowledge that your stack set template contains certain capabilities in order for AWS CloudFormation to create the stack set and related stack instances.
     */
    public readonly capabilities!: pulumi.Output<enums.cloudformation.StackSetCapability[] | undefined>;
    /**
     * A description of the stack set. You can use the description to identify the stack set's purpose or other important information.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, AWS CloudFormation uses the AWSCloudFormationStackSetExecutionRole role for the stack set operation.
     */
    public readonly executionRoleName!: pulumi.Output<string | undefined>;
    /**
     * Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.
     */
    public readonly managedExecution!: pulumi.Output<outputs.cloudformation.ManagedExecutionProperties | undefined>;
    public readonly operationPreferences!: pulumi.Output<outputs.cloudformation.StackSetOperationPreferences | undefined>;
    /**
     * The input parameters for the stack set template.
     */
    public readonly parameters!: pulumi.Output<outputs.cloudformation.StackSetParameter[] | undefined>;
    /**
     * Describes how the IAM roles required for stack set operations are created. By default, SELF-MANAGED is specified.
     */
    public readonly permissionModel!: pulumi.Output<enums.cloudformation.StackSetPermissionModel>;
    /**
     * A group of stack instances with parameters in some specific accounts and regions.
     */
    public readonly stackInstancesGroup!: pulumi.Output<outputs.cloudformation.StackSetStackInstances[] | undefined>;
    /**
     * The ID of the stack set that you're creating.
     */
    public /*out*/ readonly stackSetId!: pulumi.Output<string>;
    /**
     * The name to associate with the stack set. The name must be unique in the Region where you create your stack set.
     */
    public readonly stackSetName!: pulumi.Output<string>;
    /**
     * The key-value pairs to associate with this stack set and the stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    /**
     * The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.
     */
    public readonly templateBody!: pulumi.Output<string | undefined>;
    /**
     * Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket.
     */
    public readonly templateUrl!: pulumi.Output<string | undefined>;

    /**
     * Create a StackSet resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: StackSetArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.permissionModel === undefined) && !opts.urn) {
                throw new Error("Missing required property 'permissionModel'");
            }
            resourceInputs["administrationRoleArn"] = args ? args.administrationRoleArn : undefined;
            resourceInputs["autoDeployment"] = args ? args.autoDeployment : undefined;
            resourceInputs["callAs"] = args ? args.callAs : undefined;
            resourceInputs["capabilities"] = args ? args.capabilities : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["executionRoleName"] = args ? args.executionRoleName : undefined;
            resourceInputs["managedExecution"] = args ? args.managedExecution : undefined;
            resourceInputs["operationPreferences"] = args ? args.operationPreferences : undefined;
            resourceInputs["parameters"] = args ? args.parameters : undefined;
            resourceInputs["permissionModel"] = args ? args.permissionModel : undefined;
            resourceInputs["stackInstancesGroup"] = args ? args.stackInstancesGroup : undefined;
            resourceInputs["stackSetName"] = args ? args.stackSetName : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["templateBody"] = args ? args.templateBody : undefined;
            resourceInputs["templateUrl"] = args ? args.templateUrl : undefined;
            resourceInputs["stackSetId"] = undefined /*out*/;
        } else {
            resourceInputs["administrationRoleArn"] = undefined /*out*/;
            resourceInputs["autoDeployment"] = undefined /*out*/;
            resourceInputs["callAs"] = undefined /*out*/;
            resourceInputs["capabilities"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["executionRoleName"] = undefined /*out*/;
            resourceInputs["managedExecution"] = undefined /*out*/;
            resourceInputs["operationPreferences"] = undefined /*out*/;
            resourceInputs["parameters"] = undefined /*out*/;
            resourceInputs["permissionModel"] = undefined /*out*/;
            resourceInputs["stackInstancesGroup"] = undefined /*out*/;
            resourceInputs["stackSetId"] = undefined /*out*/;
            resourceInputs["stackSetName"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["templateBody"] = undefined /*out*/;
            resourceInputs["templateUrl"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["permissionModel", "stackSetName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(StackSet.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a StackSet resource.
 */
export interface StackSetArgs {
    /**
     * The Amazon Resource Number (ARN) of the IAM role to use to create this stack set. Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account.
     */
    administrationRoleArn?: pulumi.Input<string>;
    /**
     * Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to the target organization or organizational unit (OU). Specify only if PermissionModel is SERVICE_MANAGED.
     */
    autoDeployment?: pulumi.Input<inputs.cloudformation.StackSetAutoDeploymentArgs>;
    /**
     * Specifies the AWS account that you are acting from. By default, SELF is specified. For self-managed permissions, specify SELF; for service-managed permissions, if you are signed in to the organization's management account, specify SELF. If you are signed in to a delegated administrator account, specify DELEGATED_ADMIN.
     */
    callAs?: pulumi.Input<enums.cloudformation.StackSetCallAs>;
    /**
     * In some cases, you must explicitly acknowledge that your stack set template contains certain capabilities in order for AWS CloudFormation to create the stack set and related stack instances.
     */
    capabilities?: pulumi.Input<pulumi.Input<enums.cloudformation.StackSetCapability>[]>;
    /**
     * A description of the stack set. You can use the description to identify the stack set's purpose or other important information.
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, AWS CloudFormation uses the AWSCloudFormationStackSetExecutionRole role for the stack set operation.
     */
    executionRoleName?: pulumi.Input<string>;
    /**
     * Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.
     */
    managedExecution?: pulumi.Input<inputs.cloudformation.ManagedExecutionPropertiesArgs>;
    operationPreferences?: pulumi.Input<inputs.cloudformation.StackSetOperationPreferencesArgs>;
    /**
     * The input parameters for the stack set template.
     */
    parameters?: pulumi.Input<pulumi.Input<inputs.cloudformation.StackSetParameterArgs>[]>;
    /**
     * Describes how the IAM roles required for stack set operations are created. By default, SELF-MANAGED is specified.
     */
    permissionModel: pulumi.Input<enums.cloudformation.StackSetPermissionModel>;
    /**
     * A group of stack instances with parameters in some specific accounts and regions.
     */
    stackInstancesGroup?: pulumi.Input<pulumi.Input<inputs.cloudformation.StackSetStackInstancesArgs>[]>;
    /**
     * The name to associate with the stack set. The name must be unique in the Region where you create your stack set.
     */
    stackSetName?: pulumi.Input<string>;
    /**
     * The key-value pairs to associate with this stack set and the stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    /**
     * The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.
     */
    templateBody?: pulumi.Input<string>;
    /**
     * Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket.
     */
    templateUrl?: pulumi.Input<string>;
}

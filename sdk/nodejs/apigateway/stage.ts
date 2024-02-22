// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The ``AWS::ApiGateway::Stage`` resource creates a stage for a deployment.
 */
export class Stage extends pulumi.CustomResource {
    /**
     * Get an existing Stage resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Stage {
        return new Stage(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:apigateway:Stage';

    /**
     * Returns true if the given object is an instance of Stage.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Stage {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Stage.__pulumiType;
    }

    /**
     * Access log settings, including the access log format and access log destination ARN.
     */
    public readonly accessLogSetting!: pulumi.Output<outputs.apigateway.StageAccessLogSetting | undefined>;
    /**
     * Specifies whether a cache cluster is enabled for the stage.
     */
    public readonly cacheClusterEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * The stage's cache capacity in GB. For more information about choosing a cache size, see [Enabling API caching to enhance responsiveness](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html).
     */
    public readonly cacheClusterSize!: pulumi.Output<string | undefined>;
    /**
     * Settings for the canary deployment in this stage.
     */
    public readonly canarySetting!: pulumi.Output<outputs.apigateway.StageCanarySetting | undefined>;
    /**
     * The identifier of a client certificate for an API stage.
     */
    public readonly clientCertificateId!: pulumi.Output<string | undefined>;
    /**
     * The identifier of the Deployment that the stage points to.
     */
    public readonly deploymentId!: pulumi.Output<string | undefined>;
    /**
     * The stage's description.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The version of the associated API documentation.
     */
    public readonly documentationVersion!: pulumi.Output<string | undefined>;
    /**
     * A map that defines the method settings for a Stage resource. Keys (designated as ``/{method_setting_key`` below) are method paths defined as ``{resource_path}/{http_method}`` for an individual method override, or ``/\*&#47;\*`` for overriding all methods in the stage.
     */
    public readonly methodSettings!: pulumi.Output<outputs.apigateway.StageMethodSetting[] | undefined>;
    /**
     * The string identifier of the associated RestApi.
     */
    public readonly restApiId!: pulumi.Output<string>;
    /**
     * The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.
     */
    public readonly stageName!: pulumi.Output<string | undefined>;
    /**
     * The collection of tags. Each tag element is associated with a given resource.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    /**
     * Specifies whether active tracing with X-ray is enabled for the Stage.
     */
    public readonly tracingEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * A map (string-to-string map) that defines the stage variables, where the variable name is the key and the variable value is the value. Variable names are limited to alphanumeric characters. Values must match the following regular expression: ``[A-Za-z0-9-._~:/?#&=,]+``.
     */
    public readonly variables!: pulumi.Output<{[key: string]: string} | undefined>;

    /**
     * Create a Stage resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: StageArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.restApiId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'restApiId'");
            }
            resourceInputs["accessLogSetting"] = args ? args.accessLogSetting : undefined;
            resourceInputs["cacheClusterEnabled"] = args ? args.cacheClusterEnabled : undefined;
            resourceInputs["cacheClusterSize"] = args ? args.cacheClusterSize : undefined;
            resourceInputs["canarySetting"] = args ? args.canarySetting : undefined;
            resourceInputs["clientCertificateId"] = args ? args.clientCertificateId : undefined;
            resourceInputs["deploymentId"] = args ? args.deploymentId : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["documentationVersion"] = args ? args.documentationVersion : undefined;
            resourceInputs["methodSettings"] = args ? args.methodSettings : undefined;
            resourceInputs["restApiId"] = args ? args.restApiId : undefined;
            resourceInputs["stageName"] = args ? args.stageName : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["tracingEnabled"] = args ? args.tracingEnabled : undefined;
            resourceInputs["variables"] = args ? args.variables : undefined;
        } else {
            resourceInputs["accessLogSetting"] = undefined /*out*/;
            resourceInputs["cacheClusterEnabled"] = undefined /*out*/;
            resourceInputs["cacheClusterSize"] = undefined /*out*/;
            resourceInputs["canarySetting"] = undefined /*out*/;
            resourceInputs["clientCertificateId"] = undefined /*out*/;
            resourceInputs["deploymentId"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["documentationVersion"] = undefined /*out*/;
            resourceInputs["methodSettings"] = undefined /*out*/;
            resourceInputs["restApiId"] = undefined /*out*/;
            resourceInputs["stageName"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["tracingEnabled"] = undefined /*out*/;
            resourceInputs["variables"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["restApiId", "stageName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Stage.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Stage resource.
 */
export interface StageArgs {
    /**
     * Access log settings, including the access log format and access log destination ARN.
     */
    accessLogSetting?: pulumi.Input<inputs.apigateway.StageAccessLogSettingArgs>;
    /**
     * Specifies whether a cache cluster is enabled for the stage.
     */
    cacheClusterEnabled?: pulumi.Input<boolean>;
    /**
     * The stage's cache capacity in GB. For more information about choosing a cache size, see [Enabling API caching to enhance responsiveness](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html).
     */
    cacheClusterSize?: pulumi.Input<string>;
    /**
     * Settings for the canary deployment in this stage.
     */
    canarySetting?: pulumi.Input<inputs.apigateway.StageCanarySettingArgs>;
    /**
     * The identifier of a client certificate for an API stage.
     */
    clientCertificateId?: pulumi.Input<string>;
    /**
     * The identifier of the Deployment that the stage points to.
     */
    deploymentId?: pulumi.Input<string>;
    /**
     * The stage's description.
     */
    description?: pulumi.Input<string>;
    /**
     * The version of the associated API documentation.
     */
    documentationVersion?: pulumi.Input<string>;
    /**
     * A map that defines the method settings for a Stage resource. Keys (designated as ``/{method_setting_key`` below) are method paths defined as ``{resource_path}/{http_method}`` for an individual method override, or ``/\*&#47;\*`` for overriding all methods in the stage.
     */
    methodSettings?: pulumi.Input<pulumi.Input<inputs.apigateway.StageMethodSettingArgs>[]>;
    /**
     * The string identifier of the associated RestApi.
     */
    restApiId: pulumi.Input<string>;
    /**
     * The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.
     */
    stageName?: pulumi.Input<string>;
    /**
     * The collection of tags. Each tag element is associated with a given resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    /**
     * Specifies whether active tracing with X-ray is enabled for the Stage.
     */
    tracingEnabled?: pulumi.Input<boolean>;
    /**
     * A map (string-to-string map) that defines the stage variables, where the variable name is the key and the variable value is the value. Variable names are limited to alphanumeric characters. Values must match the following regular expression: ``[A-Za-z0-9-._~:/?#&=,]+``.
     */
    variables?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}

// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The ``AWS::ApiGateway::DocumentationVersion`` resource creates a snapshot of the documentation for an API. For more information, see [Representation of API Documentation in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api-content-representation.html) in the *API Gateway Developer Guide*.
 */
export class DocumentationVersion extends pulumi.CustomResource {
    /**
     * Get an existing DocumentationVersion resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DocumentationVersion {
        return new DocumentationVersion(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:apigateway:DocumentationVersion';

    /**
     * Returns true if the given object is an instance of DocumentationVersion.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DocumentationVersion {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DocumentationVersion.__pulumiType;
    }

    /**
     * A description about the new documentation snapshot.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The version identifier of the to-be-updated documentation version.
     */
    public readonly documentationVersion!: pulumi.Output<string>;
    /**
     * The string identifier of the associated RestApi.
     */
    public readonly restApiId!: pulumi.Output<string>;

    /**
     * Create a DocumentationVersion resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DocumentationVersionArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.documentationVersion === undefined) && !opts.urn) {
                throw new Error("Missing required property 'documentationVersion'");
            }
            if ((!args || args.restApiId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'restApiId'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["documentationVersion"] = args ? args.documentationVersion : undefined;
            resourceInputs["restApiId"] = args ? args.restApiId : undefined;
        } else {
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["documentationVersion"] = undefined /*out*/;
            resourceInputs["restApiId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["documentationVersion", "restApiId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(DocumentationVersion.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a DocumentationVersion resource.
 */
export interface DocumentationVersionArgs {
    /**
     * A description about the new documentation snapshot.
     */
    description?: pulumi.Input<string>;
    /**
     * The version identifier of the to-be-updated documentation version.
     */
    documentationVersion: pulumi.Input<string>;
    /**
     * The string identifier of the associated RestApi.
     */
    restApiId: pulumi.Input<string>;
}
